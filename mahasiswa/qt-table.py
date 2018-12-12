from PyQt5 import QtWidgets, uic, QtCore, Qt
from PyQt5.QtCore import *
from mahasiswa import Mahasiswa
from jurusan import Jurusan




class MahasiswaTableModel(QtCore.QAbstractTableModel): 
  def __init__(self, datain, headerdata, parent=None, *args): 
    """ datain: a list of lists
        headerdata: a list of strings
    """
    QtCore.QAbstractTableModel.__init__(self, parent, *args) 
    self.arraydata = datain
    self.headerdata = headerdata

  def rowCount(self, parent): 
    #   menunjukkan jumlah barisnya
    return len(self.arraydata) 

  def columnCount(self, parent): 
    # menunjukkan jumlah kolomnya
    return len(self.headerdata) 

  def data(self, index, role): 
    # isi data untuk row dan kolom
    if not index.isValid(): 
        return QVariant() 
    elif role != Qt.DisplayRole: 
        return QVariant() 
    mahasiswa = self.arraydata[index.row()]
    switcher = [mahasiswa.nim,mahasiswa.nama,mahasiswa.jurusan.jurusan]
    return QVariant(switcher[index.column()]) 

  def headerData(self, col, orientation, role):
    # membrikan title pada table
    if orientation == Qt.Horizontal and role == Qt.DisplayRole:
        return QVariant(self.headerdata[col])
        print(orientation,' ',role)
    return QVariant()

def simpanMahasiswa():
  print("simpan")
  global mahasiswa
  m = mahasiswa
  m.nim = dlg.nimLineEdit.text()
  m.nama = dlg.namaLineEdit.text()
  m.jurusan = jurusanComboBox.currentData()

  date = dlg.tanggalLahirDateEdit.date()
  tanggal = date.day()
  bulan = date.month()
  tahun = date.year()
  m.tanggal_lahir = str(tahun)+"-"+str(bulan)+"-"+str(tanggal)

  if m.id is not None:
      m.update()
  else:
      m.save()
   
  loadMahasiswa()
  mahasiswa = Mahasiswa()
  mahasiswaForm(mahasiswa)

def loadMahasiswa():
    global dataMahasiswa
    dataMahasiswa = Mahasiswa.getAll()
    tableModel = MahasiswaTableModel(dataMahasiswa,["NIM","Nama","Jurusan"])
    dlg.mahasiswaTableView.setModel(tableModel)

def doubleClicked_table():
    index = dlg.mahasiswaTableView.selectedIndexes()[0]
    mahasiswa = dataMahasiswa[index.row()]
    mahasiswaForm(mahasiswa)

def mahasiswaForm(m):
    global mahasiswa

    dlg.nimLineEdit.setText(m.nim)
    dlg.namaLineEdit.setText(m.nama)

    jurusanSelected = 0
    jurusanList = Jurusan.getAll()
    iterasi = 0
    for jurusan in jurusanList:
        if m.jurusan is not None and jurusan.id == m.jurusan.id:
            jurusanSelected = iterasi
        iterasi += 1

    dlg.jurusanComboBox.setCurrentIndex(jurusanSelected)
    mahasiswa = m

app = QtWidgets.QApplication([])
dlg = uic.loadUi("./mahasiswa.ui")

mahasiswa = Mahasiswa()
mahasiswaForm(mahasiswa)

dataMahasiswa = []
loadMahasiswa()

jurusanComboBox = dlg.jurusanComboBox
jurusanList = Jurusan.getAll()
for jurusan in jurusanList:
  jurusanComboBox.addItem(jurusan.jurusan, jurusan)

dlg.simpanPushButton.clicked.connect(simpanMahasiswa)
dlg.mahasiswaTableView.doubleClicked.connect(doubleClicked_table)

dlg.show()
app.exec()
