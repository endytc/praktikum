class mobil():
  def __init__(self,mobil):
    self.mobil = mobil
  def __str__(self):
    return (self.mobil)

class bapak():
  def __init__(self,nama):
    self.mobil = None
    self.nama = nama
  def setMobil(self,mobil):
    self.mobil = mobil

class anak(bapak):
  def __init__(self,b):
    bapak.__init__(self,b.nama)
    bapak.setMobil(self,b.mobil)
    pass

mobil = mobil("Ferrari")
b = bapak("nama")
b.nama = "Agung"

b.mobil = mobil

a = anak(b)
print(a.mobil)
