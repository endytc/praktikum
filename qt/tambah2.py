# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tambah.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tambahButton = QtWidgets.QPushButton(self.centralwidget)
        self.tambahButton.setGeometry(QtCore.QRect(120, 160, 114, 32))
        self.tambahButton.setObjectName("tambahButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 60, 16))
        self.label.setObjectName("label")
        self.angka1LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.angka1LineEdit.setGeometry(QtCore.QRect(110, 40, 113, 21))
        self.angka1LineEdit.setObjectName("angka1LineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 60, 16))
        self.label_2.setObjectName("label_2")
        self.angka2LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.angka2LineEdit.setGeometry(QtCore.QRect(110, 80, 113, 21))
        self.angka2LineEdit.setObjectName("angka2LineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 60, 16))
        self.label_3.setObjectName("label_3")
        self.hasilLabel = QtWidgets.QLabel(self.centralwidget)
        self.hasilLabel.setGeometry(QtCore.QRect(110, 120, 60, 16))
        self.hasilLabel.setObjectName("hasilLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tambahButton.clicked.connect(self.tambahkan)

    def tambahkan(self):
        print("tes")
        self.hasilLabel.setText("Cek")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tambahButton.setText(_translate("MainWindow", "Tambahkan"))
        self.label.setText(_translate("MainWindow", "Angka 1"))
        self.angka1LineEdit.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Angka 2"))
        self.angka2LineEdit.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Hasil"))
        self.hasilLabel.setText(_translate("MainWindow", "-"))


from PyQt5 import QtWidgets
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


