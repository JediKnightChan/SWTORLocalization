# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog

from gui_additional import MoveLabel, OpenLabel, MainButton
from gui_settings import Ui_settings


class Ui_Form(object):
    def __init__(self, widget_obj, supervisor_obj, tuple_for_main_button, progress_bar):
        super().__init__()
        self.widget_obj = widget_obj
        self.supervisor_obj = supervisor_obj

        self.Settings = QtWidgets.QDialog()
        self.settings_ui = Ui_settings(self, self.Settings, self.supervisor_obj)
        self.settings_ui.setupUi()

        self.leftbckgr = tuple_for_main_button[0]
        self.installdelete = tuple_for_main_button[1]

        self.progressBar = progress_bar


    def setupUi(self):
        Form = self.widget_obj
        Form.setObjectName("СВИТОР")
        Form.setWindowIcon(QIcon("Assets/icon.png"))
        Form.resize(960, 600)
        Form.setMinimumSize(QtCore.QSize(960, 600))
        Form.setMaximumSize(QtCore.QSize(960, 600))
        Form.setStyleSheet("")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTitleHint)
        self.quickWidget = QtQuickWidgets.QQuickWidget(Form)
        self.quickWidget.setGeometry(QtCore.QRect(-190, 860, 300, 200))
        self.quickWidget.setObjectName("quickWidget")
        self.mainbckgr = QtWidgets.QFrame(Form)
        self.mainbckgr.setGeometry(QtCore.QRect(0, -1, 970, 610))
        self.mainbckgr.setMinimumSize(QtCore.QSize(970, 610))
        self.mainbckgr.setMaximumSize(QtCore.QSize(970, 610))
        self.mainbckgr.setStyleSheet("background-image: url(Assets/background.jpg);")
        self.mainbckgr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainbckgr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainbckgr.setLineWidth(0)
        self.mainbckgr.setObjectName("mainbckgr")

        # adding ability to drag the window
        self.movelabel = MoveLabel(self.mainbckgr, Form)
        # self.movelabel = QtWidgets.QLabel(self.mainbckgr)
        self.movelabel.setGeometry(QtCore.QRect(0, 0, 970, 40))
        self.movelabel.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.movelabel.setText("")
        self.movelabel.setObjectName("movelabel")
        self.movelabel.raise_()


        self.pushButton_2 = QtWidgets.QPushButton(self.mainbckgr)
        self.pushButton_2.setGeometry(QtCore.QRect(828, 0, 44, 44))
        self.pushButton_2.setStyleSheet("background-image: url(Assets/settings.png);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_settings)

        self.pushButton_3 = QtWidgets.QPushButton(self.mainbckgr)
        self.pushButton_3.setGeometry(QtCore.QRect(872, 0, 44, 44))
        self.pushButton_3.setStyleSheet("background-image: url(Assets/laydown.jpg);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(Form.showMinimized)

        self.pushButton_4 = QtWidgets.QPushButton(self.mainbckgr)
        self.pushButton_4.setGeometry(QtCore.QRect(916, 0, 44, 44))
        self.pushButton_4.setStyleSheet("background-image: url(Assets/exit.jpg);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # self.leftbckgr = QtWidgets.QFrame(Form)
        self.leftbckgr.setGeometry(QtCore.QRect(0, 0, 340, 600))
        self.leftbckgr.setStyleSheet("background-color: rgb(31,40,39);")
        self.leftbckgr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftbckgr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftbckgr.setObjectName("leftbckgr")
        self.label = QtWidgets.QLabel(self.leftbckgr)
        self.label.setGeometry(QtCore.QRect(10, 50, 331, 20))
        self.label.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 12pt \"Franklin Gothic Demi\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.play = QtWidgets.QPushButton(self.leftbckgr)
        self.play.clicked.connect(self.supervisor_obj.start_game)
        self.play.setGeometry(QtCore.QRect(45, 460, 250, 60))
        self.play.setBaseSize(QtCore.QSize(0, 0))
        self.play.setAutoFillBackground(False)
        self.play.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"DIN 1451 fette Breitschrift 193\";\n"
"background-color: rgb(249,190,74);")
        self.play.setObjectName("play")
        #self.installdelete = MainButton(self.leftbckgr, self.action_list)

        self.installdelete.setGeometry(QtCore.QRect(45, 380, 250, 60))
        self.installdelete.setStyleSheet("background-color: rgb(9, 68, 177);\n"
"font: 11pt \"DIN 1451 fette Breitschrift 193\";\n"
"color: rgb(255, 255, 255);")
        self.installdelete.setObjectName("installdelete")

        self.label_2 = QtWidgets.QLabel(self.leftbckgr)
        self.label_2.setGeometry(QtCore.QRect(9, 29, 331, 21))
        self.label_2.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 12pt \"Franklin Gothic Demi\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_29 = OpenLabel(self.leftbckgr, "https://vk.com/topic-128194393_36378740")
        self.label_29.setGeometry(QtCore.QRect(5, 530, 331, 20))
        self.label_29.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 10pt \"Franklin Gothic Demi\";")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.progressBar.setGeometry(QtCore.QRect(0, 570, 340, 30))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"     border: 0px solid grey;\n"
"     background-color: #1F2827;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color:  rgb(249,190,74);\n"
" }\n"
"")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.descr = QtWidgets.QFrame(Form)
        self.descr.setGeometry(QtCore.QRect(25, 90, 290, 300))
        self.descr.setStyleSheet("QScrollBar:horizontal {\n"
"     border: 1px solid #1707ff;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #1707ff, stop: 0.5 #0c2aad, stop: 1 #0f35db);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"      \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #1707ff, stop: 1  #0c2aad);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ceb93d, stop: 0.5 #f9be4a, stop: 1  #fff70a);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"     \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      background: none;\n"
"      \n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}")
        self.descr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.descr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.descr.setObjectName("descr")
        self.scrollArea = QtWidgets.QScrollArea(self.descr)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 290, 260))
        self.scrollArea.setStyleSheet("background-color: rgb(29,43,44);\n"
"color: rgb(206, 185, 61);\n"
"font: 9pt \"Franklin Gothic Demi\";")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 795))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 31, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 34, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 32, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 14, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 17, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 25, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 16, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 18, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 24, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 29, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 30, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 20, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 23, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 21, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 13, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 19, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 12, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 22, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 15, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 26, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 33, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 27, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 36, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 35, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 28, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName("label_41")


        self.gridLayout.addWidget(self.label_41, 37, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.mainbckgr.raise_()
        self.quickWidget.raise_()
        self.leftbckgr.raise_()
        self.descr.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "СВИТОР"))
        self.supervisor_obj.reload_main_button()
        self.play.setText(_translate("Form", "ИГРАТЬ"))
        self.label_29.setText(_translate("Form",
                                         "<html><head/><body><p><span style=\" text-decoration: underline;\">Поддержать локализацию</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Русификатор"))
        self.label.setText(_translate("Form", "STAR WARS: The Old Republic"))
        self.label_13.setText(_translate("Form", "ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ"))
        self.label_3.setText(_translate("Form", "Команда локализации не несёт"))
        self.label_4.setText(_translate("Form", "ответственности за проблемы,"))
        self.label_5.setText(_translate("Form", "так или иначе связанные с "))
        self.label_6.setText(_translate("Form", "данным русификатором - "))
        self.label_7.setText(_translate("Form", "например, бан вашего игрового"))
        self.label_8.setText(_translate("Form", "аккаунта, неработоспособность "))
        self.label_9.setText(_translate("Form", "игры, системы и т. д."))
        self.label_10.setText(_translate("Form", "Пользуясь данной программой,"))
        self.label_11.setText(_translate("Form", "вы соглашаетесь с этим и берёте"))
        self.label_12.setText(_translate("Form", "всю ответственность на себя."))

        self.label_16.setText(_translate("Form", "О ПАТЧАХ"))
        self.label_18.setText(_translate("Form", "Перед загрузкой патча будет"))
        self.label_19.setText(_translate("Form", "разумно откатить перевод. Для"))
        self.label_20.setText(_translate("Form", "этого нажмите на кнопку"))
        self.label_21.setText(_translate("Form", "«Сообщить о патче». Число"))
        self.label_22.setText(_translate("Form", "сообщений о патче увеличится,"))
        self.label_23.setText(_translate("Form", "файлы игры вернутся в исходное"))
        self.label_24.setText(_translate("Form", "состояние, и вы сможете "))
        self.label_25.setText(_translate("Form", "загрузить патч. Невыполнение"))
        self.label_26.setText(_translate("Form", "данных инструкций приведёт к"))
        self.label_27.setText(_translate("Form", "тому, что игра будет полностью"))
        self.label_28.setText(_translate("Form", "переустановлена."))

        self.label_31.setText(_translate("Form", "ПОЛИТИКА РАСПРОСТРАНЕНИЯ"))
        self.label_32.setText(_translate("Form", "Русификатор распространяется"))
        self.label_34.setText(_translate("Form", "абсолютно бесплатно. Он не"))
        self.label_35.setText(_translate("Form", "должен устанавливать на ваше"))
        self.label_36.setText(_translate("Form", "устройство никакие "))
        self.label_37.setText(_translate("Form", "разновидности Malware."))
        self.label_38.setText(_translate("Form", "«Безопасные» версии этого"))
        self.label_39.setText(_translate("Form", "русификатора вы всегда можете"))
        self.label_40.setText(_translate("Form", "скачать в нашей группе в ВК или"))
        self.label_41.setText(_translate("Form", "на нашем сайте."))

    def open_settings(self):
        self.Settings.show()
