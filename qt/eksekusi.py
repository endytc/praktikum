from tambah_parse import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys 

app = QtWidgets.QApplication(sys.argv)  #buat instance baru QtGui
winForm = Ui_MainWindow()                    #inisialisasi variable winForm sebagain class Main
# winForm.show()                      #tampilkan windows form
app.exec_()