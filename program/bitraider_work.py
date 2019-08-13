import shutil
import os

from system import handle_error


class BitHandler():
    def __init__(self, supervisor):
        self.delete_dirs = ["bitraider"]
        self.supervisor = supervisor

    def check_bitraider(self):
        self.dir_game = self.supervisor.reader.get_parameter("DirGame")
        with open(self.dir_game + "launcher.settings", "r") as file_set:
            options = file_set.read()
            if ', "PatchingMode": "{ \\"swtor\\": \\"BR\\" }"' in options and ', "bitraider_disable": false' in options:
                return 0
            elif ', "PatchingMode": "{ \\"swtor\\": \\"SSN\\" }"' in options and ', "bitraider_disable": true' in options:
                return 1
            else:
                return -1

    def disable_bitraider(self):
        try:
            self.dir_game = self.supervisor.reader.get_parameter("DirGame")
            with open(self.dir_game + "launcher.settings", "r") as file_set:
                options = file_set.read()
                options = options.replace(', "PatchingMode": "{ \\"swtor\\": \\"BR\\" }"', ', "PatchingMode": "{ \\"swtor\\": \\"SSN\\" }"')
                options = options.replace(', "bitraider_disable": false', ', "bitraider_disable": true')
            with open(self.dir_game + "launcher.settings", "w") as file_set:
                file_set.write(options)

            for dir_to_remove in self.delete_dirs:
                shutil.rmtree(self.dir_game + dir_to_remove)

            os.startfile(self.dir_game + "launcher.exe")
        except Exception as e:
            handle_error(e)
            self.supervisor.raise_error(False, "Возникла непредвиденная ошибка.", "Описание доступно в логах.")

        return 1
