import vk_api
from PyQt5 import QtCore, QtWidgets

from system import handle_error


class VKLoginThread(QtCore.QThread):
    error = QtCore.pyqtSignal(str)
    close = QtCore.pyqtSignal()

    def __init__(self, browser_obj):
        QtCore.QThread.__init__(self)
        self.browser_obj = browser_obj

    def run(self):
        while "access_token" not in self.browser_obj.url().toString():
            pass
        new_url = self.browser_obj.url().toString()
        parsed_url = self.parse_url(new_url)

        vk_session = vk_api.VkApi(token=parsed_url["access_token"])

        groups = vk_session.method("groups.get")["items"]
        if 23885463 in groups:
            self.error.emit("restricted")
        else:
            print("Well")
        self.close.emit()

    def parse_url(self, url):
        result = {}
        parts = url.split("#")
        dictionary = parts[1]
        pairs = dictionary.split("&")
        for pair in pairs:
            key, value = pair.split("=")
            result[key] = value
        return result
