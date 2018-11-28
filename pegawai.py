class Penduduk():
  def __init__(self):
    self.no_ktp = None
    self.nama = None
    self.no_telp = None
  def menikah(self):
    pass

class Pegawai():
  def __init__(self):
    self.nik = None
    self.nama = None
    self.pendidikan_terakhir = None
  def menerimaGaji(self):
    pass  

class Dosen(Penduduk,Pegawai):
  def mengajar(self):
    pass
