# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'busca.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_Busca(object):
    def setupUi(self, Busca):
        Busca.setObjectName("Busca")
        Busca.resize(478, 307)
        Busca.setMinimumSize(QtCore.QSize(478, 307))
        Busca.setMaximumSize(QtCore.QSize(478, 307))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Busca.sizePolicy().hasHeightForWidth())
        Busca.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Busca.setWindowIcon(icon)
        Busca.setStyleSheet("background-color: rgb(34, 47, 62);")
        self.centralwidget = QtWidgets.QWidget(Busca)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.crawler)
        self.pushButton.setGeometry(QtCore.QRect(150, 60, 181, 71))
        self.pushButton.setStyleSheet("background-color: rgb(48, 57, 82);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 140, 181, 71))
        self.pushButton_2.clicked.connect(self.tratar)
        self.pushButton_2.setStyleSheet("background-color: rgb(48, 57, 82);")
        self.pushButton_2.setObjectName("pushButton_2")
        Busca.setCentralWidget(self.centralwidget)

        self.retranslateUi(Busca)
        QtCore.QMetaObject.connectSlotsByName(Busca)

    def crawler(self):

        os.system('xterm -e "python3 google_Dorks.py"')
        os.system('xterm -e "python3 verify_Sites.py"')
        msg = QMessageBox()
        msg.setWindowTitle("Crawler")
        msg.setText("Crawler Terminado")
        x = msg.exec_()

    def tratar(self):
        os.system('xterm -e "python3 email_tratamento.py"')
        os.system('xterm -e "python3 to_json.py"')
        msg = QMessageBox()
        msg.setWindowTitle("Tratamento")
        msg.setText("Tratamento Terminado")
        x = msg.exec_()

    def retranslateUi(self, Busca):
        _translate = QtCore.QCoreApplication.translate
        Busca.setWindowTitle(_translate("Busca", "Busca"))
        self.pushButton.setText(_translate("Busca", "Crawler"))
        self.pushButton_2.setText(_translate("Busca", "Tratar Dados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Busca = QtWidgets.QMainWindow()
    ui = Ui_Busca()
    ui.setupUi(Busca)
    Busca.show()
    sys.exit(app.exec_())

