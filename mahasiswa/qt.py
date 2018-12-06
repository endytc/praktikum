from PyQt5 import QtWidgets, uic
from mahasiswa import Mahasiswa
from jurusan import Jurusan

jurusanSelected = None

def simpanMahasiswa():
  print("simpan")
  print(jurusanSelected)
  m = Mahasiswa()
  m.nim = dlg.nimLineEdit.text()
  m.nama = dlg.namaLineEdit.text()
  m.jurusan = jurusanComboBox.currentData()
  m.tanggal_lahir = dlg.tanggalLahirDateEdit.text()
  m.save()



app = QtWidgets.QApplication([])
dlg = uic.loadUi("./mahasiswa.ui")

jurusanComboBox = dlg.jurusanComboBox
jurusanList = Jurusan.getAll()
for jurusan in jurusanList:
  jurusanComboBox.addItem(jurusan.jurusan, jurusan)

dlg.simpanPushButton.clicked.connect(simpanMahasiswa)

dlg.show()
app.exec()