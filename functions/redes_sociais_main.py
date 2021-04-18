# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redes_sociais.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setMinimumSize(QtCore.QSize(538, 348))
        MainWindow.setMaximumSize(QtCore.QSize(538, 348))
        MainWindow.setStyleSheet("background-color: rgb(34, 47, 62);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 30, 191, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 120, 191, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 210, 191, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redes Sociais"))
        self.pushButton_2.setText(_translate("MainWindow", "Telegram"))
        self.pushButton_3.setText(_translate("MainWindow", "Facebook"))
        self.pushButton_4.setText(_translate("MainWindow", "Twitter"))


    def telegram(self):

        os.system('xterm -e "python3 dorks_social.py.py"')
        os.system('xterm -e "python3 verify_Sites.py"')
        msg = QMessageBox()
        msg.setWindowTitle("Crawler")
        msg.setText("Crawler Terminado")
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

