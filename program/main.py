from PyQt5 import QtWidgets

import os
import sys

from gui_main_window import Ui_Form
from gui_additional import MainButton

from system import log_uncaught_exceptions, is_admin, handle_error
from supervisor import Supervisor
from network import Client
import ctypes

prog_ver = 0.08


def connect_to_server(supervisor_obj):
    client = Client()
    data = client.receive_server_data()
    if not data:
        print("Не удалось подключиться к серверу")
        supervisor_obj.raise_error(False, "Не удалось подключиться к серверу.", "Вы не сможете своевременно получить",
                                   "обновления к переводу.")
    else:
        print(data["patch_alerts"])
        supervisor_obj.set_num_alerts(data["patch_alerts"])

        if data["patch_confirmed"]:
            supervisor_obj.confirm_patch()

        if data["version"] > supervisor_obj.reader.get_parameter("Version"):
            print("Доступна новая версия перевода")
            try:
                if supervisor_obj.reader.get_parameter("Disk") == "Yandex":
                    supervisor_obj.download_file_yandex("trans")
                elif supervisor_obj.reader.get_parameter("Disk") == "Google":
                    supervisor_obj.download_file_google("trans")

                supervisor_obj.reader.set_parameter("Version", data["version"])
                if supervisor_obj.reader.get_parameter("TranslationInstalled"):
                    supervisor_obj.install_translation()
            except Exception as e:
                handle_error(e)
                supervisor_obj.raise_error(False, "Не удалось обновить перевод.", "Ошибка доступна в логах. Измените",
                                           "диск и перезапустите программу.")

        if data["prog_ver"] > prog_ver:
            if supervisor_obj.reader.get_parameter("TranslationInstalled"):
                supervisor_obj.restore_all_game_files()

            if supervisor_obj.reader.get_parameter("Disk") == "Yandex":
                supervisor_obj.download_file_yandex("program")
            elif supervisor_obj.reader.get_parameter("Disk") == "Google":
                supervisor_obj.download_file_google("program")
            os.startfile("setup.exe")
            sys.exit(0)


if __name__ == "__main__":

    try:
        # if True:
        sys.hook = log_uncaught_exceptions

        admin_need = False
        if admin_need:
            if not is_admin():
                try:
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                except:
                    handle_error("Отсутствуют права администратора.", False)
                finally:
                    sys.exit(0)

        supervisor = Supervisor()

        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()

        main_bckgr = QtWidgets.QFrame(Form)
        action_list = {"change_dir": supervisor.change_dir_game,
                       "install": supervisor.install_translation,
                       "disable": supervisor.disable_bitraider,
                       "delete_confirmed": supervisor.alert_patch,
                       "delete": supervisor.restore_all_game_files
                       }
        main_button = MainButton(main_bckgr, action_list)
        progress_bar = QtWidgets.QProgressBar(main_bckgr)
        supervisor.set_gui_elements(main_button, progress_bar)

        ui = Ui_Form(Form, supervisor, (main_bckgr, main_button), progress_bar)
        ui.setupUi()

        connect_to_server(supervisor)

        Form.show()
        # supervisor.login_vk()

        sys.exit(app.exec_())

    except Exception as e:
        handle_error(e)
