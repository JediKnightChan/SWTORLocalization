# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser_choise.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gui_additional import FunctionLabel

from login_vk import Authorization


class AuthDialog(object):
    def __init__(self, supervisor_obj):
        self.supervisor_obj = supervisor_obj
        self.auth_obj = Authorization(self, supervisor_obj)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        Dialog.setMinimumSize(QtCore.QSize(600, 400))
        Dialog.setMaximumSize(QtCore.QSize(600, 400))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 650, 400))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Demi\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 50, 600, 50))
        self.label.setStyleSheet("font: 16pt \"Franklin Gothic Demi\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = FunctionLabel(self.frame, self.supervisor_obj.close_login_dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 320, 600, 50))
        self.label_5.setStyleSheet("font: 10pt \"Franklin Gothic Demi\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label")
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(100, 150, 100, 100))
        self.frame_2.setStyleSheet("background-image: url(Assets/chrome.png);\n"
"border-style: none;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(250, 150, 100, 105))
        self.frame_3.setStyleSheet("background-image: url(Assets/firefox.png);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(400, 150, 100, 100))
        self.frame_4.setStyleSheet("background-image: url(Assets/chromium.png);\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = FunctionLabel(self.frame, self.auth_obj.authorize_chrome)
        self.label_2.setGeometry(QtCore.QRect(100, 275, 100, 30))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = FunctionLabel(self.frame, self.auth_obj.authorize_firefox)
        self.label_3.setGeometry(QtCore.QRect(250, 275, 100, 30))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = FunctionLabel(self.frame, self.authorize_app_browser)
        self.label_4.setGeometry(QtCore.QRect(400, 275, 100, 30))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вход в ВК"))
        self.label.setText(_translate("Dialog", "Выберите браузер для авторизации через ВК"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Chrome</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Firefox</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Русификатор</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Не проходить авторизацию</span></p></body></html>"))

    def close_login_dialog(self):
        self.login_dialog.accept()
        self.supervisor_obj.close_login_dialog()

    def authorize_app_browser(self):
        pass
