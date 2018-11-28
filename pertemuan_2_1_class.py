class mahasiswa():

    def __init__(self,nama,jurusan):
        self.__nama = nama
        self.jurusan = jurusan

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self,nama):
        self.__nama = nama
    
    def get_nama(self):
        return self.__nama
    
m = mahasiswa("Siti Aminah","Teknik Informatika")
# print(m.__nama)
print (m.get_nama())
print (m.jurusan)


