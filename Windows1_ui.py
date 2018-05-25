# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Windows1.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Windows2_ui import Ui_Dialog
    
class Ui_MainWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, -30, 781, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Users/Dika/Videos/79667412-mini-margarita-pizza-italian-food-simple-background-fast-food.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(760, 30, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 100, 1241, 361))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 480, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(940, 550, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Users/Dika/Pictures/35927b20e857475eecb3586d6229c877_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(70, 200))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-4, 0, 591, 771))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../../../Users/Dika/Documents/79667412-mini-margarita-pizza-italian-food-simple-background-fast-food.jpg"))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.openWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Basal Metabolic Rate (BMR)</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#020202;\">Basal Metabolic Rate (BMR) adalah jumlah kalori yang dibutuhkan </span></p><p><span style=\" color:#020202;\">tubuh untuk menjalankan fungsi jantung, otak, ginjal, dan organ-</span></p><p><span style=\" color:#020202;\">organ lain, saat Anda tidak bergerak sama sekali.<br/></span></p><p><span style=\" color:#020202;\">Namun, BMR saja tidak cukup untuk mengetahui kebutuhan kalori </span></p><p><span style=\" color:#020202;\">harian Anda karena BMR tidak mempertimbangkan faktor aktivitas </span></p><p><span style=\" color:#020202;\">fisik. Tubuh Anda juga membutuhkan energi (kalori) untuk </span></p><p><span style=\" color:#020202;\">melakukan berbagai aktivitas fisik sehari-hari, seperti berjalan,</span></p><p><span style=\" color:#020202;\">bekerja, dan berolahraga.</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#090909;\">Silahkan klik tombol di bawah ini untuk menghitung kalori anda.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

