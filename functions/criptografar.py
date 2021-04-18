# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criptografar.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 298)
        MainWindow.setMinimumSize(QtCore.QSize(527, 298))
        MainWindow.setMaximumSize(QtCore.QSize(527, 298))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(34, 47, 62);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 30, 191, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.encrypt)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Criptografar"))
        self.pushButton.setText(_translate("MainWindow", "Criptografar"))


    def encrypt():
        os.system('xterm -e python3 encrypt.py')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

