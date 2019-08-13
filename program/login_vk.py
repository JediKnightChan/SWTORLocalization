from selenium import webdriver
import requests
import vk_api

from PyQt5 import QtCore, QtWidgets
from gui_additional import Dialog
from system import handle_error
import profiles


# In this thread we wait until VK grants us an access token
class URLThread(QtCore.QThread):
    error = QtCore.pyqtSignal(str)
    close = QtCore.pyqtSignal()

    def __init__(self, browser_type, code_url):
        QtCore.QThread.__init__(self)
        self.browser_type = browser_type
        self.code_url = code_url

    def create_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir={}".format(profiles.get_chrome_user_dir()))
        options.add_argument("--app=https://www.google.com")
        self.browser_obj = webdriver.Chrome(chrome_options=options)

    def create_firefox(self):
        fp = webdriver.FirefoxProfile(profiles.get_firefox_profile_dir())
        self.browser_obj = webdriver.Firefox(firefox_profile=fp)

    def get_code_url(self):
        while type(self.browser_obj.current_url) is not str or "code" not in self.browser_obj.current_url:
            pass
        url_with_code = self.browser_obj.current_url
        self.browser_obj.quit()
        return url_with_code

    def run(self):
        try:
            if self.browser_type == "chrome":
                self.create_chrome()
            elif self.browser_type == "firefox":
                self.create_firefox()
            self.browser_obj.get(self.code_url)

            url_with_code = self.get_code_url()
            code = self.parse_url(url_with_code)["code"]
            print(code)
            token_url = "https://oauth.vk.com/access_token?client_id=1&client_secret=1" \
                        "&redirect_uri=https://oauth.vk.com/blank.html&code={}".format(code)
            response = requests.get(token_url)
            access_token = response.json()["access_token"]

            vk_session = vk_api.VkApi(token=access_token)
            groups = vk_session.method("groups.get")["items"]
            if 23885463 in groups:
                self.error.emit("restricted")
            else:
                print("well")
            self.close.emit()
        except Exception as e:
            self.error.emit("browser")
            handle_error(e)

    def parse_url(self, url):
        result = {}
        parts = url.split("#")
        dictionary = parts[1]
        pairs = dictionary.split("&")
        for pair in pairs:
            key, value = pair.split("=")
            result[key] = value
        return result


class Authorization(QtCore.QObject):
    def __init__(self, widget, supervisor_obj):
        super().__init__()
        self.code_url = "https://oauth.vk.com/authorize?client_id=1" \
                        "&redirect_uri=https://oauth.vk.com/blank.html&display=page&scope=groups&response_type=code&v=5.59"
        self.widget = widget
        self.supervisor_obj = supervisor_obj

    def authorize_chrome(self):
        self.auth_thread = URLThread("chrome", self.code_url)
        self.start_auth_thread()


    def authorize_firefox(self):
        self.auth_thread = URLThread("firefox", self.code_url)
        self.start_auth_thread()

    def start_auth_thread(self):
        self.auth_thread.start()
        self.auth_thread.error.connect(self.call_error)
        self.auth_thread.close.connect(self.supervisor_obj.close_login_dialog)

    @QtCore.pyqtSlot(str)
    def call_error(self, error_name):
        if error_name == "restricted":
            print("Свтор онлайн")
            self.supervisor_obj.raise_error(True, "Подписчикам сообщества swtor.online",
                                            "ограничен доступ к русификатору.")
        elif error_name == "browser":
            self.supervisor_obj.raise_error(False, "Не удалось авторизоваться через",
                                            "этот браузер. Ошибка доступна в",
                                            "логах")
