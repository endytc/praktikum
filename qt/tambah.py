from PyQt5 import QtWidgets, uic


def tambahkan():
  angka1 = float(dlg.angka1LineEdit.text())
  angka2 = float(dlg.angka2LineEdit.text())
  hasil = angka1 + angka2
  dlg.hasilLabel.setText(str(hasil))

app = QtWidgets.QApplication([])

dlg = uic.loadUi("./tambah.ui")
dlg.tambahButton.clicked.connect(tambahkan)
dlg.show()

app.exec()