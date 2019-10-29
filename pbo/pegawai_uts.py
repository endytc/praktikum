class Pegawai():
  def __init__(self):
    self.nama = None
    self.gaji_pokok = None
    self.uang_makan = 50000
    self.presensi = 0

  def presensi(self):
    self.presensi+=1

  def hitungGaji(self):
    print("lengkapi")

class ProjectManajer(Pegawai):
  def __init__(self):
    self.tunjangan_jabatan = 5000000


class Designer(Pegawai):
  def hitungGaji(self):
    print("gaji pokok+screen*100000")

class ProjectManajer(Pegawai):
  def hitungGaji(self):
    print("gaji pokok+jumlah project*1000000")

class Programmer(Pegawai):
  def hitungGaji(self):
    print("gaji pokok+task*100000")
    
class Tester(Pegawai):
  def hitungGaji(self):
    print("gaji pokok+task*100000")
pegawaiList = list()

p = Programmer()
pegawaiList.append(p)

d = Designer()
pegawaiList.append(d)
t = Tester()
pegawaiList.append(t)
for pegawai in pegawaiList:
  pegawai.hitungGaji()