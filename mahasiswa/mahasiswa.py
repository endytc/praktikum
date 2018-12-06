from conn import DBConnection
from datetime import datetime
from jurusan import Jurusan

class Mahasiswa():
  def __init__(self):
    self.id = None
    self.nama = None
    self.nim = None
    self.tanggal_lahir = None
    self.jurusan = None
    self.created_at = datetime.today()

  def save(self):
    query = ("INSERT INTO mahasiswa (id_jurusan, nim, nama, tanggal_lahir, created_at) values"
            "(%(id_jurusan)s,%(nim)s,%(nama)s,%(tanggal_lahir)s,%(created_at)s)")
    conn = DBConnection.get_conn()
    cursor = conn.cursor()
    data = {
      "id_jurusan": self.jurusan.id,
      "nim": self.nim,
      "nama": self.nama,
      "tanggal_lahir": self.tanggal_lahir,
      "created_at": self.created_at
    }
    cursor.execute(query,data)
    self.id = conn.insert_id()
    conn.commit()
  
  def update(self):
    query = ("update mahasiswa "
            "set id_jurusan = %(id_jurusan)s, nim = %(nim)s,nama = %(nama)s,"
            "tanggal_lahir = %(tanggal_lahir)s, updated_at = %(updated_at)s where id = %(id)s")
    conn = DBConnection.get_conn()
    cursor = conn.cursor()
    data = {
      "id": self.id,
      "id_jurusan": self.jurusan.id,
      "nim": self.nim,
      "nama": self.nama,
      "tanggal_lahir": self.tanggal_lahir,
      "updated_at": datetime.today(),
    }
    cursor.execute(query,data)
    conn.commit()
  
  def delete(self):
    query = ("delete from mahasiswa where id = %(id)s")
    conn = DBConnection.get_conn()
    cursor = conn.cursor()
    data = {
      "id": self.id
    }
    cursor.execute(query,data)
    conn.commit()

    print("Mahaswiswa berhasil dihapus")

  @staticmethod
  def getAll():
    query = ("select id,id_jurusan,nim,nama,tanggal_lahir,created_at,updated_at from mahasiswa")
    conn = DBConnection.get_conn()
    cursor = conn.cursor()
    cursor.execute(query)

    mahasiswaResult = []
    results = cursor.fetchall()
    for result in results:
      mahasiswa = mahasiswa()
      mahasiswa.id = result[0]
      mahasiswa.jurusan = Jurusan.find(result[1])
      mahasiswa.nim = result[2]
      mahasiswa.nama = result[3]
      mahasiswa.tanggal_lahir = result[4]
      mahasiswa.created_at = result[5]
      mahasiswa.updated_at = result[6]
      mahasiswaResult.append(mahasiswa)
      
    return mahasiswaResult


mahasiswa = Mahasiswa()
mahasiswa.nim = "0001"
mahasiswa.nama = "Eko Sulistiyono"
mahasiswa.jurusan = Jurusan.find(21)
mahasiswa.tanggal_lahir = "1999-02-01"
mahasiswa.save()