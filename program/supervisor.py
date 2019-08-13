import os
import json
from zipfile import ZipFile

from PyQt5.QtCore import QCoreApplication, QThread, pyqtSignal, pyqtSlot, QObject, QUrl
from PyQt5.QtWidgets import QFileDialog, QWidget, QDialog

from gui_additional import Dialog
from gui_error import Ui_Error

from options_reader import Reader
from network import Client
from system import handle_error, txt_file_to_dict
from assets_reader import AssetsSupervisor
from bitraider_work import BitHandler
from game_work import TorEditor
from web_yandex import YaDisk
from web_google import GoogleDisk
from browser_choise import AuthDialog


class Supervisor():
    def __init__(self):
        self.reader = Reader()
        self.tor_editor = TorEditor(self.reader)
        self.patch_confirmed = False
        self.num_alerts = 0
        self.bit_handler = BitHandler(self)
        self.client = None
        self.main_button = None
        assets_supervisor = AssetsSupervisor()
        assets_supervisor.check_dir()

    def set_gui_elements(self, main_button, progress_bar):
        self.main_button = main_button
        self.progress_bar = progress_bar

    def confirm_patch(self):
        self.patch_confirmed = True

    def set_num_alerts(self, n):
        self.num_alerts = n
        self.reload_main_button()

    def start_game(self):
        if self.reader.get_parameter("TranslationInstalled") and self.reader.get_parameter("DisableBitraider") == False:
            self.restore_all_game_files()
        dir_game = self.reader.get_parameter("DirGame")
        try:
            os.startfile(dir_game + "launcher.exe")
        except FileNotFoundError:
            handle_error("Не найден launcher.exe в {}".format(dir_game), False)
            self.raise_error(False, "Лаунчер игры не обнаружен.", "Проверьте указанную папку с игрой.")

    def raise_error(self, auto_close, a="", b="", c=""):
        self.Error = Dialog(auto_close)
        self.uie = Ui_Error(self.Error)
        self.uie.setupUi(self.Error, a, b, c)
        self.Error.setModal(True)
        self.Error.show()

    def login_vk(self):
        self.login_dialog = QDialog()
        self.login_dialog.setModal(True)
        self.login_ui = AuthDialog(self)
        self.login_ui.setupUi(self.login_dialog)
        self.login_dialog.show()

    def close_login_dialog(self):
        self.login_dialog.accept()

    def reload_main_button(self):
        try:
            if self.reader.get_parameter("DirGame") == "/":
                self.main_button.setText("Указать папку с игрой")
                self.main_button.set_action("change_dir")
            elif not self.reader.get_parameter("TranslationInstalled"):
                if self.bit_handler.check_bitraider() == 1 or self.reader.get_parameter("DisableBitraider") == False:
                    self.main_button.setText("Установить перевод")
                    self.main_button.set_action("install")
                else:
                    self.main_button.setText("Отключить BitRaider")
                    self.main_button.set_action("disable")
            elif self.patch_confirmed:
                self.main_button.setText("Откатить перевод (Патч)")
                self.main_button.set_action("delete_confirmed")
            else:
                self.main_button.setText("Сообщить о патче ({})".format(self.num_alerts))
                self.main_button.set_action("delete")
        except Exception as e:
            handle_error(e)
            self.main_button.setText("Указать папку с игрой")
            self.main_button.set_action("change_dir")

    def backup_game_files(self, game_archives):
        try:
            self.tor_editor.backup(game_archives)
        except FileNotFoundError:
            self.raise_error(False, "Не удалось откатить перевод.", "Возможно, папка с игрой указана неверно.")
        except Exception as e:
            handle_error(e)

    def restore_game_files(self, game_archives):
        try:
            self.tor_editor.restore(game_archives)
        except FileNotFoundError:
            self.raise_error(False, "Не удалось откатить перевод.", "Возможно, папка с игрой указана", "неверно.")
        except Exception as e:
            handle_error(e)

    def install_translation(self):
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)

        cnt_files = 0
        try:
            zip_file = ZipFile("trans.zip", "r")
            zip_file.setpassword(b"iz20Wo4suqmUcZHFXL8G")

            with zip_file.open("assets.json") as file_assets_to_backup:
                assets_to_backup = json.load(file_assets_to_backup)
                self.set_archives_to_restore(list(assets_to_backup.values()))
            QCoreApplication.processEvents()

            if self.reader.get_parameter("TranslationInstalled"):
                self.tor_editor.restore(assets_to_backup.values())
            else:
                self.tor_editor.backup(assets_to_backup.values())
            QCoreApplication.processEvents()

            with zip_file.open("settings.txt") as manager_file:
                game_files = txt_file_to_dict(manager_file)

            delta = 100 / len(game_files)

            for game_path in game_files:
                archive = None
                for game_dir in assets_to_backup:
                    if game_dir in game_path:
                        archive = assets_to_backup[game_dir]
                        print(archive)
                with zip_file.open(game_files[game_path]) as game_file:
                    cnt_files += self.tor_editor.change_file_in_tor(game_file.read(), game_path, archive)
                self.progress_bar.setValue(int(cnt_files * delta))
                QCoreApplication.processEvents()

            print("{} файлов успешно добавлено в игру".format(cnt_files))
            self.progress_bar.setValue(0)

            zip_file.extract("info.txt")
            self.reader.set_parameter("TranslationInstalled", True)
            self.reload_main_button()
        except FileNotFoundError as e:
            handle_error(e)
            self.raise_error(False, "Возникла ошибка: не найден файл.", "Подробности в логах.")
        except Exception as e:
            handle_error(e)
            self.raise_error(False, "Возникла непредвиденная ошибка.", "Подробности в логах.")

    def get_archives_to_restore(self):
        try:
            with open("Backup/arcs.json") as f:
                return json.load(f)
        except FileNotFoundError:
            self.raise_error(False, "Не найден файл бэкапа.")

    def set_archives_to_restore(self, list_):
        with open("Backup/arcs.json", "w") as f:
            json.dump(list_, f)

    def alert_patch(self):
        try:
            self.client = Client()
            self.client.alert_patch()
            self.restore_all_game_files()
            self.start_game()
        except Exception as e:
            handle_error(e)

    def restore_all_game_files(self):
        try:
            archives = self.get_archives_to_restore()
            self.restore_game_files(archives)
            self.reader.set_parameter("TranslationInstalled", False)
            QCoreApplication.processEvents()
        except Exception as e:
            handle_error(e)
        finally:
            self.reload_main_button()

    def change_dir_game(self):
        dir_game = str(QFileDialog.getExistingDirectory(caption="Пожалуйста, укажите папку с игрой")) + "/"
        if dir_game == "/":
            self.raise_error(False, "Папка с игрой указана на была.", "Пожалуйста, попробуйте снова.")
        else:
            self.reader.set_parameter("DirGame", dir_game)

        try:
            self.bit_handler.check_bitraider()
        except FileNotFoundError:
            self.raise_error(False, "Не удалось проверить состояние", "BitRaider. Убедитесь, что указана",
                             "именно игровая папка.")
        self.reload_main_button()

    def download_file_yandex(self, file):
        self.download_file_google(file)

    def download_file_google(self, file):
        google = GoogleDisk()
        if file == "trans":
            google.download_translation()
        elif file == "program":
            google.download_program()

    def disable_bitraider(self):
        self.bit_handler.disable_bitraider()
        self.reload_main_button()
