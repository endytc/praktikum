from conn import DBConnection
from datetime import datetime


class Jurusan():
  def __init__(self,jurusan = None):
    self.id = None
    self.jurusan = jurusan
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

  @staticmethod
  def getAll():
    query = ("select * from jurusan")
    conn = DBConnection.get_conn()
    cursor = conn.cursor()
    cursor.execute(query)

    jurusanResult = []
    results = cursor.fetchall()
    for result in results:
      jurusan = Jurusan()
      jurusan.id = result[0]
      jurusan.jurusan = result[1]
      jurusan.created_at = result[2]
      jurusan.updated_at = result[3]
      jurusanResult.append(jurusan)
    return jurusanResult


# jurusan  = Jurusan("Teknik Informatika")
# jurusan.save()

# jurusan.jurusan = "Seni"
# jurusan.update()

# jurusan.delete()

jurusanList = Jurusan.getAll()
print (len(jurusanList))