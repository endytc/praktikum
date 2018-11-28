from conn import DBConnection
from datetime import datetime


class Mahasiswa():
  def __init__(self,jurusan):
    self.id = None
    self.jurusan = None
    self.created_at = datetime.today()

  def save(self):
    query = ("INSERT INTO jurusan (jurusan, created_at) values"
            "(%(jurusan)s,%(created_at)s)")
    conn = DBConnection.get_conn()
    cursor = conn.cursor()
    data = {
      "jurusan": self.jurusan,
      "created_at": self.created_at
    }
    cursor.execute(query,data)
    self.id = conn.insert_id()
    conn.commit()
  
  def update(self):
    query = ("update jurusan "
            "set jurusan = %(jurusan)s, updated_at = %(updated_at)s where id = %(id)s")
    conn = DBConnection.get_conn()
    cursor = conn.cursor()
    data = {
      "jurusan": self.jurusan,
      "updated_at": datetime.today(),
      "id": self.id
    }
    cursor.execute(query,data)
    conn.commit()
  
  def delete(self):
    query = ("delete from jurusan where id = %(id)s")
    conn = DBConnection.get_conn()
    cursor = conn.cursor()
    data = {
      "id": self.id
    }
    cursor.execute(query,data)
    conn.commit()

    print("Jurusan berhasil dihapus")





jurusan  = Jurusan("Teknik Informatika")
jurusan.save()

jurusan.jurusan = "Seni"
jurusan.update()

jurusan.delete()