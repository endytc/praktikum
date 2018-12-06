from abc import ABC, abstractmethod
class Pegawai(ABC):
  def presensi(self):
    print("melakukan presensi menggunakan sidik jari")

  @abstractmethod
  def hitungGaji(self):
    pass
  

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