from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QAction, QDialog, qApp


class Ui_Error(QDialog):
    def __init__(self, widget_obj):
        super().__init__()
        self.widget_obj = widget_obj

    def setupUi(self, Error, text1, text2, text3=""):
        Error.setWindowTitle("Ошибка")
        exitAction = QAction(self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        Error.setObjectName("Error")
        Error.resize(300, 200)
        Error.setMinimumSize(QtCore.QSize(300, 200))
        Error.setMaximumSize(QtCore.QSize(300, 200))
        self.butok = QtWidgets.QPushButton(Error)
        self.butok.setGeometry(QtCore.QRect(100, 140, 100, 30))
        self.butok.setObjectName("butok")
        self.butok.clicked.connect(self.widget_obj.close)
        self.mainframe = QtWidgets.QFrame(Error)
        self.mainframe.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.mainframe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.errordesc = QtWidgets.QLabel(self.mainframe)
        self.errordesc.setGeometry(QtCore.QRect(90, 50, 200, 20))
        self.errordesc.setObjectName("errordesc")
        self.label = QtWidgets.QLabel(self.mainframe)
        self.label.setGeometry(QtCore.QRect(90, 70, 200, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.mainframe)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 200, 20))
        self.label_2.setObjectName("label_2")
        self.errordesc.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.butok.raise_()
        self.pngframe = QtWidgets.QFrame(Error)
        self.pngframe.setGeometry(QtCore.QRect(30, 60, 40, 40))
        self.pngframe.setStyleSheet("background-image: url(Assets/error.png);\n"
"")
        self.pngframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pngframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pngframe.setObjectName("pngframe")
        self.mainframe.raise_()
        self.butok.raise_()
        self.pngframe.raise_()

        self.retranslateUi(Error, text1, text2, text3)
        self.close()
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error, text1, text2, text3=""):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Dialog"))
        self.errordesc.setText(_translate("Error", text1))
        self.label.setText(_translate("Error", text2))
        self.label_2.setText(_translate("Error", text3))
        self.butok.setText(_translate("Error", "ОК"))
