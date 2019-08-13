# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newset.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from gui_additional import OpenLabel


class Ui_settings(QWidget):
	def __init__(self, main_gui_obj, widget_obj, supervisor_obj):
		super().__init__()
		self.main_gui_obj = main_gui_obj
		self.widget_obj = widget_obj
		self.supervisor_obj = supervisor_obj

	def setupUi(self):
		settingstor = self.widget_obj
		settingstor.setObjectName("settingstor")
		settingstor.setEnabled(True)
		settingstor.resize(960, 600)
		settingstor.setMinimumSize(QtCore.QSize(960, 600))
		settingstor.setMaximumSize(QtCore.QSize(960, 600))

		self.pushButton = QtWidgets.QPushButton(settingstor)
		self.pushButton.setEnabled(True)
		self.pushButton.setGeometry(QtCore.QRect(670, 530, 125, 40))
		self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"font: 75 11pt \"DIN 1451 fette Breitschrift 193\";\n"
"background-color: rgb(244,201,71);")
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.save_settings)

		self.pushButton_3 = QtWidgets.QPushButton(settingstor)
		self.pushButton_3.clicked.connect(self.supervisor_obj.alert_patch)
		self.pushButton_3.setEnabled(True)
		self.pushButton_3.setGeometry(QtCore.QRect(20, 530, 180, 40))
		self.pushButton_3.setStyleSheet("background-color: rgb(9, 68, 177);\n"
"font: 11pt \"DIN 1451 fette Breitschrift 193\";\n"
"color: rgb(255, 255, 255);")
		self.pushButton_3.setObjectName("pushButton_3")
		self.frame_3 = QtWidgets.QFrame(settingstor)
		self.frame_3.setEnabled(True)
		self.frame_3.setGeometry(QtCore.QRect(815, 530, 125, 40))
		self.frame_3.setStyleSheet("background-color: rgb(255, 208, 17);")
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
		self.pushButton_2.clicked.connect(self.close_settings)
		self.pushButton_2.setEnabled(True)
		self.pushButton_2.setGeometry(QtCore.QRect(1, 1, 123, 38))
		self.pushButton_2.setStyleSheet("color: rgb(244,201,71);\n"
"font: 75 11pt \"DIN 1451 fette Breitschrift 193\";\n"
"background-color: rgb(31,40,39);")
		self.pushButton_2.setObjectName("pushButton_2")
		self.frame = QtWidgets.QFrame(settingstor)
		self.frame.setEnabled(True)
		self.frame.setGeometry(QtCore.QRect(0, 0, 960, 600))
		self.frame.setStyleSheet("background-color: rgb(31,40,39);")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.frame_2 = QtWidgets.QFrame(self.frame)
		self.frame_2.setEnabled(True)
		self.frame_2.setGeometry(QtCore.QRect(20, 20, 920, 480))
		self.frame_2.setStyleSheet("QScrollBar:horizontal {\n"
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
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #ceb93d;\n"
"    width: 20px;\n"
"}\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
		self.scrollArea.setEnabled(True)
		self.scrollArea.setGeometry(QtCore.QRect(0, 0, 911, 500))
		self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setEnabled(True)
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -356, 902, 854))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
		self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.frame_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
		self.frame_9.setEnabled(True)
		self.frame_9.setMinimumSize(QtCore.QSize(0, 450))
		self.frame_9.setMaximumSize(QtCore.QSize(16777215, 450))
		self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_9.setObjectName("frame_9")
		self.label_403 = QtWidgets.QLabel(self.frame_9)
		self.label_403.setEnabled(True)
		self.label_403.setGeometry(QtCore.QRect(0, 75, 238, 20))
		self.label_403.setMinimumSize(QtCore.QSize(0, 20))
		self.label_403.setMaximumSize(QtCore.QSize(250, 20))
		self.label_403.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 12pt \"Franklin Gothic Demi\";")
		self.label_403.setObjectName("label_403")
		self.label_405 = QtWidgets.QLabel(self.frame_9)
		self.label_405.setEnabled(True)
		self.label_405.setGeometry(QtCore.QRect(0, 161, 150, 20))
		self.label_405.setMinimumSize(QtCore.QSize(0, 20))
		self.label_405.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_405.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_405.setObjectName("label_405")
		self.label_406 = QtWidgets.QLabel(self.frame_9)
		self.label_406.setEnabled(True)
		self.label_406.setGeometry(QtCore.QRect(0, 104, 238, 20))
		self.label_406.setMinimumSize(QtCore.QSize(0, 20))
		self.label_406.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_406.setText("")
		self.label_406.setObjectName("label_406")
		self.label_407 = QtWidgets.QLabel(self.frame_9)
		self.label_407.setEnabled(True)
		self.label_407.setGeometry(QtCore.QRect(0, 56, 238, 20))
		self.label_407.setMinimumSize(QtCore.QSize(0, 20))
		self.label_407.setMaximumSize(QtCore.QSize(16777215, 10))
		self.label_407.setText("")
		self.label_407.setObjectName("label_407")
		self.label_408 = QtWidgets.QLabel(self.frame_9)
		self.label_408.setEnabled(True)
		self.label_408.setGeometry(QtCore.QRect(0, 132, 150, 20))
		self.label_408.setMinimumSize(QtCore.QSize(0, 20))
		self.label_408.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_408.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_408.setObjectName("label_408")
		self.label_409 = QtWidgets.QLabel(self.frame_9)
		self.label_409.setEnabled(True)
		self.label_409.setGeometry(QtCore.QRect(0, 306, 150, 20))
		self.label_409.setMinimumSize(QtCore.QSize(0, 20))
		self.label_409.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_409.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_409.setObjectName("label_409")
		self.label_410 = QtWidgets.QLabel(self.frame_9)
		self.label_410.setEnabled(True)
		self.label_410.setGeometry(QtCore.QRect(0, 335, 150, 20))
		self.label_410.setMinimumSize(QtCore.QSize(0, 20))
		self.label_410.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_410.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_410.setObjectName("label_410")
		self.label_411 = QtWidgets.QLabel(self.frame_9)
		self.label_411.setEnabled(True)
		self.label_411.setGeometry(QtCore.QRect(0, 248, 150, 20))
		self.label_411.setMinimumSize(QtCore.QSize(0, 20))
		self.label_411.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_411.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_411.setObjectName("label_411")
		self.label_412 = QtWidgets.QLabel(self.frame_9)
		self.label_412.setEnabled(True)
		self.label_412.setGeometry(QtCore.QRect(0, 27, 200, 20))
		self.label_412.setMinimumSize(QtCore.QSize(0, 20))
		self.label_412.setMaximumSize(QtCore.QSize(200, 20))
		self.label_412.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 12pt \"Franklin Gothic Demi\";")
		self.label_412.setObjectName("label_412")
		self.label_413 = QtWidgets.QLabel(self.frame_9)
		self.label_413.setEnabled(True)
		self.label_413.setGeometry(QtCore.QRect(0, 219, 150, 20))
		self.label_413.setMinimumSize(QtCore.QSize(0, 20))
		self.label_413.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_413.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_413.setObjectName("label_413")
		self.label_414 = QtWidgets.QLabel(self.frame_9)
		self.label_414.setEnabled(True)
		self.label_414.setGeometry(QtCore.QRect(0, 190, 150, 20))
		self.label_414.setMinimumSize(QtCore.QSize(0, 20))
		self.label_414.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_414.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_414.setObjectName("label_414")
		self.label_583 = QtWidgets.QLabel(self.frame_9)
		self.label_583.setEnabled(True)
		self.label_583.setGeometry(QtCore.QRect(650, 219, 200, 20))
		self.label_583.setMinimumSize(QtCore.QSize(200, 0))
		self.label_583.setMaximumSize(QtCore.QSize(200, 20))
		self.label_583.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_583.setObjectName("label_583")
		self.label_584 = QtWidgets.QLabel(self.frame_9)
		self.label_584.setEnabled(True)
		self.label_584.setGeometry(QtCore.QRect(650, 323, 200, 19))
		self.label_584.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_584.setText("")
		self.label_584.setObjectName("label_584")
		self.label_586 = QtWidgets.QLabel(self.frame_9)
		self.label_586.setEnabled(True)
		self.label_586.setGeometry(QtCore.QRect(650, 309, 200, 20))
		self.label_586.setMinimumSize(QtCore.QSize(200, 0))
		self.label_586.setMaximumSize(QtCore.QSize(200, 20))
		self.label_586.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_586.setObjectName("label_586")
		self.label_587 = QtWidgets.QLabel(self.frame_9)
		self.label_587.setEnabled(True)
		self.label_587.setGeometry(QtCore.QRect(650, 120, 200, 20))
		self.label_587.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_587.setText("")
		self.label_587.setObjectName("label_587")
		self.label_588 = QtWidgets.QLabel(self.frame_9)
		self.label_588.setEnabled(True)
		self.label_588.setGeometry(QtCore.QRect(650, 190, 200, 20))
		self.label_588.setMinimumSize(QtCore.QSize(200, 0))
		self.label_588.setMaximumSize(QtCore.QSize(200, 20))
		self.label_588.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_588.setObjectName("label_588")
		self.label_589 = QtWidgets.QLabel(self.frame_9)
		self.label_589.setEnabled(True)
		self.label_589.setGeometry(QtCore.QRect(650, 294, 200, 20))
		self.label_589.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_589.setText("")
		self.label_589.setObjectName("label_589")
		self.label_590 = QtWidgets.QLabel(self.frame_9)
		self.label_590.setEnabled(True)
		self.label_590.setGeometry(QtCore.QRect(650, 248, 200, 20))
		self.label_590.setMinimumSize(QtCore.QSize(200, 0))
		self.label_590.setMaximumSize(QtCore.QSize(200, 20))
		self.label_590.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_590.setObjectName("label_590")
		self.label_585 = QtWidgets.QLabel(self.frame_9)
		self.label_585.setEnabled(True)
		self.label_585.setGeometry(QtCore.QRect(209, 190, 200, 20))
		self.label_585.setMinimumSize(QtCore.QSize(200, 0))
		self.label_585.setMaximumSize(QtCore.QSize(200, 20))
		self.label_585.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_585.setObjectName("label_585")
		self.label_591 = QtWidgets.QLabel(self.frame_9)
		self.label_591.setEnabled(True)
		self.label_591.setGeometry(QtCore.QRect(209, 219, 200, 20))
		self.label_591.setMinimumSize(QtCore.QSize(200, 0))
		self.label_591.setMaximumSize(QtCore.QSize(200, 20))
		self.label_591.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_591.setObjectName("label_591")
		self.label_592 = QtWidgets.QLabel(self.frame_9)
		self.label_592.setEnabled(True)
		self.label_592.setGeometry(QtCore.QRect(209, 338, 200, 20))
		self.label_592.setMinimumSize(QtCore.QSize(200, 0))
		self.label_592.setMaximumSize(QtCore.QSize(200, 20))
		self.label_592.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_592.setObjectName("label_592")
		self.label_593 = QtWidgets.QLabel(self.frame_9)
		self.label_593.setEnabled(True)
		self.label_593.setGeometry(QtCore.QRect(209, 248, 200, 20))
		self.label_593.setMinimumSize(QtCore.QSize(200, 0))
		self.label_593.setMaximumSize(QtCore.QSize(200, 20))
		self.label_593.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_593.setObjectName("label_593")
		self.label_594 = QtWidgets.QLabel(self.frame_9)
		self.label_594.setEnabled(True)
		self.label_594.setGeometry(QtCore.QRect(209, 161, 200, 20))
		self.label_594.setMinimumSize(QtCore.QSize(200, 0))
		self.label_594.setMaximumSize(QtCore.QSize(200, 20))
		self.label_594.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_594.setObjectName("label_594")
		self.label_595 = QtWidgets.QLabel(self.frame_9)
		self.label_595.setEnabled(True)
		self.label_595.setGeometry(QtCore.QRect(209, 309, 200, 20))
		self.label_595.setMinimumSize(QtCore.QSize(200, 0))
		self.label_595.setMaximumSize(QtCore.QSize(200, 20))
		self.label_595.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_595.setObjectName("label_595")
		self.label_596 = QtWidgets.QLabel(self.frame_9)
		self.label_596.setEnabled(True)
		self.label_596.setGeometry(QtCore.QRect(209, 132, 200, 20))
		self.label_596.setMinimumSize(QtCore.QSize(200, 0))
		self.label_596.setMaximumSize(QtCore.QSize(200, 20))
		self.label_596.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_596.setObjectName("label_596")
		self.label_597 = QtWidgets.QLabel(self.frame_9)
		self.label_597.setEnabled(True)
		self.label_597.setGeometry(QtCore.QRect(209, 277, 200, 20))
		self.label_597.setMinimumSize(QtCore.QSize(200, 0))
		self.label_597.setMaximumSize(QtCore.QSize(200, 20))
		self.label_597.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_597.setObjectName("label_597")
		self.label_598 = QtWidgets.QLabel(self.frame_9)
		self.label_598.setEnabled(True)
		self.label_598.setGeometry(QtCore.QRect(468, 161, 150, 20))
		self.label_598.setMinimumSize(QtCore.QSize(150, 0))
		self.label_598.setMaximumSize(QtCore.QSize(150, 20))
		self.label_598.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_598.setObjectName("label_598")
		self.label_599 = QtWidgets.QLabel(self.frame_9)
		self.label_599.setEnabled(True)
		self.label_599.setGeometry(QtCore.QRect(468, 190, 150, 20))
		self.label_599.setMinimumSize(QtCore.QSize(150, 0))
		self.label_599.setMaximumSize(QtCore.QSize(150, 20))
		self.label_599.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_599.setObjectName("label_599")
		self.label_600 = QtWidgets.QLabel(self.frame_9)
		self.label_600.setEnabled(True)
		self.label_600.setGeometry(QtCore.QRect(468, 219, 150, 20))
		self.label_600.setMinimumSize(QtCore.QSize(150, 0))
		self.label_600.setMaximumSize(QtCore.QSize(150, 20))
		self.label_600.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_600.setObjectName("label_600")
		self.label_601 = QtWidgets.QLabel(self.frame_9)
		self.label_601.setEnabled(True)
		self.label_601.setGeometry(QtCore.QRect(468, 248, 150, 20))
		self.label_601.setMinimumSize(QtCore.QSize(150, 0))
		self.label_601.setMaximumSize(QtCore.QSize(150, 20))
		self.label_601.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_601.setObjectName("label_601")
		self.label_602 = QtWidgets.QLabel(self.frame_9)
		self.label_602.setEnabled(True)
		self.label_602.setGeometry(QtCore.QRect(468, 309, 150, 20))
		self.label_602.setMinimumSize(QtCore.QSize(150, 0))
		self.label_602.setMaximumSize(QtCore.QSize(150, 20))
		self.label_602.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_602.setObjectName("label_602")
		self.label_604 = QtWidgets.QLabel(self.frame_9)
		self.label_604.setEnabled(True)
		self.label_604.setGeometry(QtCore.QRect(0, 369, 150, 20))
		self.label_604.setMinimumSize(QtCore.QSize(0, 20))
		self.label_604.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_604.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_604.setObjectName("label_604")
		self.label_605 = QtWidgets.QLabel(self.frame_9)
		self.label_605.setEnabled(True)
		self.label_605.setGeometry(QtCore.QRect(209, 369, 200, 20))
		self.label_605.setMinimumSize(QtCore.QSize(200, 0))
		self.label_605.setMaximumSize(QtCore.QSize(200, 20))
		self.label_605.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_605.setObjectName("label_605")
		self.label_606 = QtWidgets.QLabel(self.frame_9)
		self.label_606.setEnabled(True)
		self.label_606.setGeometry(QtCore.QRect(468, 369, 150, 20))
		self.label_606.setMinimumSize(QtCore.QSize(150, 0))
		self.label_606.setMaximumSize(QtCore.QSize(150, 20))
		self.label_606.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_606.setObjectName("label_606")
		self.label_607 = QtWidgets.QLabel(self.frame_9)
		self.label_607.setEnabled(True)
		self.label_607.setGeometry(QtCore.QRect(650, 369, 200, 20))
		self.label_607.setMinimumSize(QtCore.QSize(200, 0))
		self.label_607.setMaximumSize(QtCore.QSize(200, 20))
		self.label_607.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_607.setObjectName("label_607")
		self.label_610 = OpenLabel(self.frame_9, "www.youtube.com/channel/UCq3OueoADMdxxYs_Oauodog")
		self.label_610.setEnabled(True)
		self.label_610.setGeometry(QtCore.QRect(30, 410, 71, 20))
		self.label_610.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_610.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_610.setObjectName("label_610")
		self.label_610.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.VK = OpenLabel(self.frame_9, "https://vk.com/jediknightchannel")
		self.VK.setEnabled(True)
		self.VK.setGeometry(QtCore.QRect(0, 410, 21, 20))
		self.VK.setMaximumSize(QtCore.QSize(16777215, 20))
		self.VK.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.VK.setObjectName("VK")
		self.VK.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.label_611 = QtWidgets.QLabel(self.frame_9)
		self.label_611.setEnabled(True)
		self.label_611.setGeometry(QtCore.QRect(650, 277, 200, 20))
		self.label_611.setMinimumSize(QtCore.QSize(200, 0))
		self.label_611.setMaximumSize(QtCore.QSize(200, 20))
		self.label_611.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_611.setObjectName("label_611")
		self.label_603 = QtWidgets.QLabel(self.frame_9)
		self.label_603.setEnabled(True)
		self.label_603.setGeometry(QtCore.QRect(650, 338, 200, 20))
		self.label_603.setMinimumSize(QtCore.QSize(200, 0))
		self.label_603.setMaximumSize(QtCore.QSize(200, 20))
		self.label_603.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_603.setObjectName("label_603")
		self.gridLayout_3.addWidget(self.frame_9, 2, 0, 1, 1)
		self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
		self.frame_4.setEnabled(True)
		self.frame_4.setMinimumSize(QtCore.QSize(0, 380))
		self.frame_4.setMaximumSize(QtCore.QSize(16777215, 380))
		self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_4.setObjectName("frame_4")
		self.label_133 = QtWidgets.QLabel(self.frame_4)
		self.label_133.setEnabled(True)
		self.label_133.setGeometry(QtCore.QRect(554, 329, 200, 20))
		self.label_133.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_133.setText("")
		self.label_133.setObjectName("label_133")
		self.label_206 = QtWidgets.QLabel(self.frame_4)
		self.label_206.setEnabled(True)
		self.label_206.setGeometry(QtCore.QRect(554, 280, 200, 10))
		self.label_206.setMaximumSize(QtCore.QSize(16777215, 10))
		self.label_206.setText("")
		self.label_206.setObjectName("label_206")
		self.label_210 = QtWidgets.QLabel(self.frame_4)
		self.label_210.setEnabled(True)
		self.label_210.setGeometry(QtCore.QRect(20, 388, 238, 10))
		self.label_210.setMaximumSize(QtCore.QSize(16777215, 10))
		self.label_210.setText("")
		self.label_210.setObjectName("label_210")
		self.label_212 = QtWidgets.QLabel(self.frame_4)
		self.label_212.setEnabled(True)
		self.label_212.setGeometry(QtCore.QRect(0, 0, 238, 20))
		self.label_212.setMaximumSize(QtCore.QSize(250, 20))
		self.label_212.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 12pt \"Franklin Gothic Demi\";")
		self.label_212.setObjectName("label_212")
		self.comboBox_36 = QtWidgets.QComboBox(self.frame_4)
		self.comboBox_36.setEnabled(True)
		self.comboBox_36.setGeometry(QtCore.QRect(325, 248, 240, 23))
		self.comboBox_36.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic\";")
		self.comboBox_36.setObjectName("comboBox_36")
		self.comboBox_36.addItem("")
		self.comboBox_36.addItem("")
		self.label_214 = QtWidgets.QLabel(self.frame_4)
		self.label_214.setEnabled(True)
		self.label_214.setGeometry(QtCore.QRect(325, 219, 240, 20))
		self.label_214.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_214.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_214.setObjectName("label_214")
		self.comboBox_37 = QtWidgets.QComboBox(self.frame_4)
		self.comboBox_37.setEnabled(True)
		self.comboBox_37.setGeometry(QtCore.QRect(0, 168, 240, 23))
		self.comboBox_37.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic\";")
		self.comboBox_37.setObjectName("comboBox_37")
		self.comboBox_37.addItem("")
		self.comboBox_37.addItem("")
		self.label_226 = QtWidgets.QLabel(self.frame_4)
		self.label_226.setEnabled(True)
		self.label_226.setGeometry(QtCore.QRect(650, 219, 200, 20))
		self.label_226.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_226.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_226.setObjectName("label_226")
		self.label_229 = QtWidgets.QLabel(self.frame_4)
		self.label_229.setEnabled(True)
		self.label_229.setGeometry(QtCore.QRect(306, 388, 200, 10))
		self.label_229.setMaximumSize(QtCore.QSize(16777215, 10))
		self.label_229.setText("")
		self.label_229.setObjectName("label_229")
		self.comboBox_38 = QtWidgets.QComboBox(self.frame_4)
		self.comboBox_38.setEnabled(True)
		self.comboBox_38.setGeometry(QtCore.QRect(0, 78, 238, 23))
		self.comboBox_38.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic\";")
		self.comboBox_38.setObjectName("comboBox_38")
		self.comboBox_38.addItem("")
		self.comboBox_38.addItem("")
		self.comboBox_38.addItem("")
		self.label_230 = QtWidgets.QLabel(self.frame_4)
		self.label_230.setEnabled(True)
		self.label_230.setGeometry(QtCore.QRect(554, 388, 200, 10))
		self.label_230.setMaximumSize(QtCore.QSize(16777215, 10))
		self.label_230.setText("")
		self.label_230.setObjectName("label_230")
		self.label_231 = QtWidgets.QLabel(self.frame_4)
		self.label_231.setEnabled(True)
		self.label_231.setGeometry(QtCore.QRect(650, 138, 200, 21))
		self.label_231.setMaximumSize(QtCore.QSize(200, 16777215))
		self.label_231.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_231.setObjectName("label_231")
		self.comboBox_39 = QtWidgets.QComboBox(self.frame_4)
		self.comboBox_39.setEnabled(True)
		self.comboBox_39.setGeometry(QtCore.QRect(0, 328, 240, 23))
		self.comboBox_39.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic\";")
		self.comboBox_39.setObjectName("comboBox_39")
		self.comboBox_39.addItem("")
		self.comboBox_39.addItem("")
		self.comboBox_39.addItem("")
		self.label_233 = QtWidgets.QLabel(self.frame_4)
		self.label_233.setEnabled(True)
		self.label_233.setGeometry(QtCore.QRect(325, 138, 200, 20))
		self.label_233.setMinimumSize(QtCore.QSize(200, 0))
		self.label_233.setMaximumSize(QtCore.QSize(200, 20))
		self.label_233.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_233.setObjectName("label_233")
		self.comboBox_40 = QtWidgets.QComboBox(self.frame_4)
		self.comboBox_40.setEnabled(True)
		self.comboBox_40.setGeometry(QtCore.QRect(650, 248, 200, 23))
		self.comboBox_40.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic\";")
		self.comboBox_40.setObjectName("comboBox_40")
		self.comboBox_40.addItem("")
		self.comboBox_40.addItem("")
		self.label_234 = QtWidgets.QLabel(self.frame_4)
		self.label_234.setEnabled(True)
		self.label_234.setGeometry(QtCore.QRect(0, 50, 238, 20))
		self.label_234.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_234.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_234.setObjectName("label_234")
		self.comboBox_41 = QtWidgets.QComboBox(self.frame_4)
		self.comboBox_41.setEnabled(True)
		self.comboBox_41.setGeometry(QtCore.QRect(0, 248, 240, 23))
		self.comboBox_41.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic\";")
		self.comboBox_41.setObjectName("comboBox_41")
		self.comboBox_41.addItem("")
		self.comboBox_41.addItem("")
		self.label_235 = QtWidgets.QLabel(self.frame_4)
		self.label_235.setEnabled(True)
		self.label_235.setGeometry(QtCore.QRect(554, 110, 200, 19))
		self.label_235.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_235.setText("")
		self.label_235.setObjectName("label_235")
		self.label_237 = QtWidgets.QLabel(self.frame_4)
		self.label_237.setEnabled(True)
		self.label_237.setGeometry(QtCore.QRect(554, 299, 200, 20))
		self.label_237.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_237.setText("")
		self.label_237.setObjectName("label_237")
		self.label_238 = QtWidgets.QLabel(self.frame_4)
		self.label_238.setEnabled(True)
		self.label_238.setGeometry(QtCore.QRect(0, 138, 240, 20))
		self.label_238.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_238.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_238.setObjectName("label_238")
		self.comboBox_42 = QtWidgets.QComboBox(self.frame_4)
		self.comboBox_42.setEnabled(True)
		self.comboBox_42.setGeometry(QtCore.QRect(650, 168, 200, 23))
		self.comboBox_42.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic\";")
		self.comboBox_42.setObjectName("comboBox_42")
		self.comboBox_42.addItem("")
		self.comboBox_42.addItem("")
		self.comboBox_43 = QtWidgets.QComboBox(self.frame_4)
		self.comboBox_43.setEnabled(True)
		self.comboBox_43.setGeometry(QtCore.QRect(325, 168, 240, 23))
		self.comboBox_43.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic\";")
		self.comboBox_43.setObjectName("comboBox_43")
		self.comboBox_43.addItem("")
		self.comboBox_43.addItem("")
		self.comboBox_43.addItem("")
		self.label_239 = QtWidgets.QLabel(self.frame_4)
		self.label_239.setEnabled(True)
		self.label_239.setGeometry(QtCore.QRect(0, 299, 240, 20))
		self.label_239.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_239.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_239.setObjectName("label_239")
		self.label_241 = QtWidgets.QLabel(self.frame_4)
		self.label_241.setEnabled(True)
		self.label_241.setGeometry(QtCore.QRect(0, 219, 240, 20))
		self.label_241.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_241.setStyleSheet("color: rgb(206, 185, 61);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_241.setObjectName("label_241")
		self.label_404 = QtWidgets.QLabel(self.frame_4)
		self.label_404.setEnabled(True)
		self.label_404.setGeometry(QtCore.QRect(175, 50, 240, 20))
		self.label_404.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_404.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 11pt \"Franklin Gothic Demi\";")
		self.label_404.setObjectName("label_404")
		self.gridLayout_3.addWidget(self.frame_4, 1, 0, 1, 1)
		self.frame_4.raise_()
		self.frame_9.raise_()
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.pushButton_4 = QtWidgets.QPushButton(self.frame)
		self.pushButton_4.clicked.connect(self.supervisor_obj.change_dir_game)
		self.pushButton_4.setEnabled(True)
		self.pushButton_4.setGeometry(QtCore.QRect(220, 530, 180, 40))
		self.pushButton_4.setStyleSheet("background-color: rgb(9, 68, 177);\n"
"font: 11pt \"DIN 1451 fette Breitschrift 193\";\n"
"color: rgb(255, 255, 255);")
		self.pushButton_4.setObjectName("pushButton_4")

		self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
		self.frame_5.setMinimumSize(QtCore.QSize(0, 150))
		self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_5.setObjectName("frame_5")
		self.label_213 = QtWidgets.QLabel(self.frame_5)
		self.label_213.setEnabled(True)
		self.label_213.setGeometry(QtCore.QRect(0, 0, 200, 20))
		self.label_213.setMaximumSize(QtCore.QSize(250, 20))
		self.label_213.setStyleSheet("color: rgb(206, 185, 61);\n"
									 "font: 12pt \"Franklin Gothic Demi\";")
		self.label_213.setObjectName("label_213")
		self.comboBox_44 = QtWidgets.QComboBox(self.frame_5)
		self.comboBox_44.setEnabled(True)
		self.comboBox_44.setGeometry(QtCore.QRect(0, 80, 238, 23))
		self.comboBox_44.setStyleSheet("color: rgb(206, 185, 61);\n"
									   "font: 11pt \"Franklin Gothic\";")
		self.comboBox_44.setObjectName("comboBox_44")
		self.comboBox_44.addItem("")
		self.comboBox_44.addItem("")
		self.label_236 = QtWidgets.QLabel(self.frame_5)
		self.label_236.setEnabled(True)
		self.label_236.setGeometry(QtCore.QRect(0, 50, 238, 20))
		self.label_236.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_236.setStyleSheet("color: rgb(206, 185, 61);\n"
									 "font: 11pt \"Franklin Gothic Demi\";")
		self.label_236.setObjectName("label_236")
		self.label_240 = QtWidgets.QLabel(self.frame_5)
		self.label_240.setEnabled(True)
		self.label_240.setGeometry(QtCore.QRect(325, 50, 238, 20))
		self.label_240.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_240.setStyleSheet("color: rgb(206, 185, 61);\n"
									 "font: 11pt \"Franklin Gothic Demi\";")
		self.label_240.setObjectName("label_240")
		self.comboBox_45 = QtWidgets.QComboBox(self.frame_5)
		self.comboBox_45.setEnabled(True)
		self.comboBox_45.setGeometry(QtCore.QRect(325, 80, 238, 23))
		self.comboBox_45.setStyleSheet("color: rgb(206, 185, 61);\n"
									   "font: 11pt \"Franklin Gothic\";")
		self.comboBox_45.setObjectName("comboBox_45")
		self.comboBox_45.addItem("")
		self.comboBox_45.addItem("")
		self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)

		self.frame_5.raise_()
		self.frame.raise_()
		self.pushButton.raise_()
		self.pushButton_3.raise_()
		self.frame_3.raise_()

		self.retranslateUi(settingstor)
		QtCore.QMetaObject.connectSlotsByName(settingstor)

	def retranslateUi(self, settingstor):
		_translate = QtCore.QCoreApplication.translate
		settingstor.setWindowTitle(_translate("settingstor", "Настройки"))
		self.pushButton.setText(_translate("settingstor", "Сохранить"))
		self.pushButton_3.setText(_translate("settingstor", "Откатить перевод"))
		self.pushButton_2.setText(_translate("settingstor", "Выйти"))
		self.label_403.setText(_translate("settingstor", "Команда локализации"))
		self.label_405.setText(_translate("settingstor", "Togruth"))
		self.label_408.setText(_translate("settingstor", "SWTOR Jedipedia"))
		self.label_409.setText(_translate("settingstor", "Mortemus"))
		self.label_410.setText(_translate("settingstor", "Smol Potato"))
		self.label_411.setText(_translate("settingstor", "Jedi Knight"))
		self.label_412.setText(_translate("settingstor", "Информация"))
		self.label_413.setText(_translate("settingstor", "Demetrius"))
		self.label_414.setText(_translate("settingstor", "SWTOR по-русски"))
		self.label_583.setText(_translate("settingstor", "Сюжет консула"))
		self.label_586.setText(_translate("settingstor", "Сюжет воина"))
		self.label_588.setText(_translate("settingstor", "Дополнения"))
		self.label_590.setText(_translate("settingstor", "Сюжет инквизитора, рыцаря,"))
		self.label_585.setText(_translate("settingstor", "Перевод"))
		self.label_591.setText(_translate("settingstor", "Перевод"))
		self.label_592.setText(_translate("settingstor", "Перевод"))
		self.label_593.setText(_translate("settingstor", "Перевод"))
		self.label_594.setText(_translate("settingstor", "Технические вопросы"))
		self.label_595.setText(_translate("settingstor", "Перевод"))
		self.label_596.setText(_translate("settingstor", "Технические вопросы"))
		self.label_597.setText(_translate("settingstor", "Технические вопросы"))
		self.label_598.setText(_translate("settingstor", "YouTube"))
		self.label_599.setText(_translate("settingstor", "YouTube"))
		self.label_600.setText(_translate("settingstor", "Вукипедия"))
		self.label_601.setText(_translate("settingstor", "YouTube"))
		self.label_602.setText(_translate("settingstor", "Вукипедия"))
		self.label_604.setText(_translate("settingstor", "Sightsaber"))
		self.label_605.setText(_translate("settingstor", "Перевод"))
		self.label_606.setText(_translate("settingstor", "Перевод"))
		self.label_607.setText(_translate("settingstor", "Сюжет солдата"))
		self.label_610.setText(_translate("settingstor", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">YouTube</span></p></body></html>"))
		self.VK.setText(_translate("settingstor", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">ВК</span></p></body></html>"))
		self.label_611.setText(_translate("settingstor", "контрабандиста"))
		self.label_603.setText(_translate("settingstor", "Сюжет агента, охотника"))
		self.label_212.setText(_translate("settingstor", "Настройки перевода"))
		self.comboBox_36.setItemText(0, _translate("settingstor", "Инфопланшет"))
		self.comboBox_36.setItemText(1, _translate("settingstor", "Датапад"))
		self.label_214.setText(_translate("settingstor", "Datapad"))
		self.comboBox_37.setItemText(0, _translate("settingstor", "Сит"))
		self.comboBox_37.setItemText(1, _translate("settingstor", "Ситх"))
		self.label_226.setText(_translate("settingstor", "Khem Val"))
		self.comboBox_38.setItemText(0, _translate("settingstor", "2"))
		self.comboBox_38.setItemText(1, _translate("settingstor", "3"))
		self.comboBox_38.setItemText(2, _translate("settingstor", "1"))
		self.label_231.setText(_translate("settingstor", "Satele Shan"))
		self.comboBox_39.setItemText(0, _translate("settingstor", "Кворрен"))
		self.comboBox_39.setItemText(1, _translate("settingstor", "Куаррен"))
		self.comboBox_39.setItemText(2, _translate("settingstor", "Кваррен"))
		self.label_233.setText(_translate("settingstor", "Darth Nihilus"))
		self.comboBox_40.setItemText(0, _translate("settingstor", "Кхем Вал"))
		self.comboBox_40.setItemText(1, _translate("settingstor", "Кем Вал"))
		self.label_234.setText(_translate("settingstor", "Вариант локализации"))
		self.comboBox_41.setItemText(0, _translate("settingstor", "Взломщик"))
		self.comboBox_41.setItemText(1, _translate("settingstor", "Ледоруб"))
		self.label_238.setText(_translate("settingstor", "Sith"))
		self.comboBox_42.setItemText(0, _translate("settingstor", "Сатил Шан"))
		self.comboBox_42.setItemText(1, _translate("settingstor", "Сатель Шан"))
		self.comboBox_43.setItemText(0, _translate("settingstor", "Дарт Нигилус"))
		self.comboBox_43.setItemText(1, _translate("settingstor", "Дарт Нихилус"))
		self.comboBox_43.setItemText(2, _translate("settingstor", "Дарт Найлус"))
		self.label_239.setText(_translate("settingstor", "Quarren"))
		self.label_241.setText(_translate("settingstor", "Slicer"))
		self.label_404.setText(_translate("settingstor", "Временно недоступно"))
		self.pushButton_4.setText(_translate("settingstor", "Изменить папку"))

		self.label_213.setText(_translate("settingstor", "Настройки русификатора"))
		self.label_236.setText(_translate("settingstor", "Отключать BitRaider"))

		# Setting order of items in comboboxes of program settings
		if self.supervisor_obj.reader.get_parameter("DisableBitraider") == True:
			comboBox_44_items_order = {"Да": 0, "Нет": 1}
		else:
			comboBox_44_items_order = {"Да": 1, "Нет": 0}
		self.comboBox_44.setItemText(comboBox_44_items_order["Да"], _translate("settingstor", "Да"))
		self.comboBox_44.setItemText(comboBox_44_items_order["Нет"], _translate("settingstor", "Нет"))

		self.label_240.setText(_translate("settingstor", "Скачивание перевода"))
		if self.supervisor_obj.reader.get_parameter("Disk") == "Yandex":
			comboBox_45_items_order = {"Yandex": 0, "Google": 1}
		else:
			comboBox_45_items_order = {"Yandex": 1, "Google": 0}
		self.comboBox_45.setItemText(comboBox_45_items_order["Yandex"], _translate("settingstor", "Яндекс.Диск"))
		self.comboBox_45.setItemText(comboBox_45_items_order["Google"], _translate("settingstor", "Google Диск"))

	def close_settings(self):
		self.widget_obj.close()

	def save_settings(self):
		# Saving program settings
		if self.comboBox_45.currentText().strip() == "Яндекс.Диск":
			self.supervisor_obj.reader.set_parameter("Disk", "Yandex")
		elif self.comboBox_45.currentText().strip() == "Google Диск":
			self.supervisor_obj.reader.set_parameter("Disk", "Google")

		if self.comboBox_44.currentText().strip() == "Да":
			self.supervisor_obj.reader.set_parameter("DisableBitraider", True)
		elif self.comboBox_44.currentText().strip() == "Нет":
			self.supervisor_obj.reader.set_parameter("DisableBitraider", False)

		self.supervisor_obj.reload_main_button()
		# Closing settings window
		self.close_settings()
