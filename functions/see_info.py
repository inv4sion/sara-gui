# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'see_info.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 314)
        icon = QtGui.QIcon()
        MainWindow.setMinimumSize(QtCore.QSize(521, 314))
        MainWindow.setMaximumSize(QtCore.QSize(521, 314))
        icon.addPixmap(QtGui.QPixmap("logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(34, 47, 62);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.chrome)
        self.pushButton.setGeometry(QtCore.QRect(165, 30, 191, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(165, 120, 191, 81))
        self.pushButton_2.clicked.connect(self.firefox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(165, 210, 191, 81))
        self.pushButton_3.clicked.connect(self.pdf)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def chrome(self):
        os.system("./new_tab_c.sh")
        msg = QMessageBox()
        msg.setWindowTitle("Aberto")
        msg.setText("Abrindo no Chrome...")
        x = msg.exec_()
    def firefox(self):
        os.system("./new_tab_f.sh") 
        msg = QMessageBox()
        msg.setWindowTitle("Aberto")
        msg.setText("Abrindo no Firefox...")
        x = msg.exec_()
    def pdf(self):
        os.system("xterm -e python3 pdf_gen.py")
        os.system("xterm -e 'mv emails.pdf ../data'")
        msg = QMessageBox()
        msg.setWindowTitle("PDF")
        msg.setText("PDF Gerado")
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visualizar Informações"))
        self.pushButton.setText(_translate("MainWindow", "Chrome"))
        self.pushButton_2.setText(_translate("MainWindow", "Firefox"))
        self.pushButton_3.setText(_translate("MainWindow", "PDF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

