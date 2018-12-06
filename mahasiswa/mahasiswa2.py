from conn import DBConnection
from datetime import datetime

class Mahasiswa():
  def __init__(self):
    self.nim = None
    self.nama = None
    self.jurusan = None
    self.tanggal_lahir = None