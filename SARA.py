# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 705)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(652, 705))
        MainWindow.setMaximumSize(QtCore.QSize(652, 705))
        font = QtGui.QFont()
        font.setItalic(False)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(34, 47, 62);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 241, 71))
        self.pushButton.clicked.connect(self.busca)
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #2C3A47;\n"
"color: rgb(238, 238, 236);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 150, 241, 71))
        self.pushButton_2.clicked.connect(self.see_info)
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #2C3A47;\n"
"color: rgb(238, 238, 236);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 230, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #2C3A47;\n"
"color: rgb(238, 238, 236);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.redes_sociais)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 230, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(16)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 50, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(27)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(238, 238, 236);")
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 230, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: #2C3A47;\n"
"color: rgb(238, 238, 236);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.validar)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 440, 201, 191))
        self.label_2.setStyleSheet("background-image: url(:/logo/logo2.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def busca(self):
        os.system("cd functions && python3 busca.py")

    def see_info(self):
        os.system("cd functions&& python3 see_info.py")
    def redes_sociais(self):
        #os.system("cd functions && python3 redes_sociais_main.py")
        #os.system('xterm -e "cd functions && python3 dorks_social.py.py"')
        #os.system('xterm -e "cd functions && python3 verify_Sites.py"')
        os.system("cd functions && python3 busca.py")
    def criptografar(self):
        os.system("cd functions && python3 criptografar.py")
    def validar(self):
        os.system("cd functions && python3 validar.py")
    def upload(self):
        os.system("cd functions && python3 upload.py")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "S.A.R.A"))
        self.pushButton.setText(_translate("MainWindow", "Busca de Dados"))
        self.pushButton_2.setText(_translate("MainWindow", "Visualizar Informações"))
        self.pushButton_3.setText(_translate("MainWindow", "Redes Sociais"))
        self.label.setText(_translate("MainWindow", "S.A.R.A"))
        self.pushButton_5.setText(_translate("MainWindow", "Validar Informações"))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

