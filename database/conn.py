import MySQLdb


'''
  attribute connection dibuat static untuk mencegah terjadinya banyak koneksi / 
  cukup menggunakan 1 koneksi
'''
class DBConnection():
  conn = None
  def __init__():
    pass
  
  @staticmethod
  def get_conn():
    # jika koneksi belum dibuat, maka buat terlebih dahulu
    if DBConnection.conn is None:
      print("Open connection")
      cnx = MySQLdb.connect(user='root', password='',
                              host='127.0.0.1',
                              database='pbo_python')
      DBConnection.conn = cnx
    return DBConnection.conn

  def close():
    print("Close connection")
    DBConnection.conn.close()