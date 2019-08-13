from PyQt5.QtWidgets import QLabel, QDialog, QPushButton
from PyQt5 import QtCore
import webbrowser


# A label used to move a window - moving_obj
class MoveLabel(QLabel):

    def __init__(self, frame, moving_obj):
        super().__init__(frame)
        self.moving_obj = moving_obj

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.x = x - x_w
        self.y = y - y_w
        self.moving_obj.move(self.x, self.y)


# A label used to open a link in the browser
class OpenLabel(QLabel):
    def __init__(self, frame, link):
        super().__init__(frame)
        self.link = link

    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        webbrowser.open(self.link)


class FunctionLabel(QLabel):
    def __init__(self, frame, func):
        super().__init__(frame)
        self.func = func

    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.func()


# The Dialog that cannot be closed without closing the main window
class Dialog(QDialog):
    def __init__(self, auto_close):
        super().__init__()
        self.auto_close = auto_close

    def closeEvent(self, event):
        if self.auto_close:
            QtCore.QCoreApplication.instance().quit()

    def keyPressEvent(self, QKeyEvent):
        pass


# A button that can do several things
class MainButton(QPushButton):
    def __init__(self, background, action_list):
        super().__init__(background)
        self.action = None
        self.action_list = action_list

    def set_action(self, action):
        self.action = action
        self.reload_action()

    def reload_action(self):
        try:
            self.clicked.disconnect()
        except TypeError:
            pass
        self.clicked.connect(self.action_list[self.action])
