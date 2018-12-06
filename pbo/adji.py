from abc import ABC, abstractmethod

class Storage(ABC):
  @staticmethod
  def simpan():
    file=open(self.get_file(),"")
    for key,data in self.get_data():
      data=file.write("%s: %s \n"%(key,data))

  @abstractmethod
  def get_file(self):
      pass

  @abstractmethod
  def get_data(self):
      pass

class Makanan(Storage):
  def __init__(self,nama,menu,harga,bayar):
    self.nama = nama
    self.menu = menu
    self.harga = harga
    self.bayar = bayar
    self.file = "pesan_makanan.txt"
  
  def get_data(self):
    dictMakanan = {
      "nama": self.nama,
      "menu": self.menu,
      "harga": self.harga,
      "bayar": self.bayar,
    }
    return dictMakanan

  def get_file(self):
    return self.file
    
def simpan_data(nama,kamar,jml_hari,per_mlm,bayar):
	file=open("pesan_kamar.txt","a")
	data=file.write("nama: %s \n"%(nama))
	data=file.write("kamar: %s \n"%(kamar))
	data=file.write("jml_hari: %i \n"%(jml_hari))
	data=file.write("per_mlm: %i \n"%(per_mlm))
	data=file.write("bayar: %i \n"%(bayar))
def option():
	print("Pilihlah Salah Satu dibawah Ini: ")
	print("1. Pesan makanan")
	print("2. Pesan Kamar")
	print("3. Keluar Program")
	pilihan=int(input("Masukan pilihan Anda: "))
	return pilihan
	
#main program
pilihan= True
while(pilihan<3):
	pilihan= option()
	if (pilihan==3): 
		break;

	if(pilihan==1): 
		print()
		print("MENU: ")
		print("1.Nasi Goreng")
		print("2.Mie Goreng")
		print("3.Soto")
		print("4.Rawon")
		print()
		nama= str(input("Masukan Nama: "))
		menu= str(input("Masukan Menu: "))
		harga= int(input("Masukan Harga: Rp."))
		jb = int(input("Jumlah Pesan: "))
		total = harga * jb
		print("Total yang anda bayar adalah Rp.",total)
		bayar = int(input("Uang yang dibayar: Rp. "))
		if (bayar>total):
			print("Jumlah Kembalian: Rp.", bayar-total)
			makanan = Makanan(nama,menu,harga,bayar)
			makanan.simpan()
			print()
			print(". . .TERIMA KASIH. . .")
		print("-------- Menyimpan Data ---------\n")
		print()

	if(pilihan==2): 
		print("Pesan Kamar")
		nama= str(input("Masukan Nama: "))
		kamar= str(input("No Kamar: "))
		per_mlm= 500000
		jml_hari = int(input("Hari: "))
		print("Per hari: Rp.",per_mlm)
		total = per_mlm * jml_hari
		print("Total yang anda bayar adalah Rp.",total)
		bayar = int(input("Uang yang dibayar: Rp. "))
		if (bayar>total):
			print("Jumlah Kembalian: Rp.", bayar-total)
			print()
			print(". . .TERIMA KASIH. . .")
		simpan_data(nama,kamar,jml_hari,per_mlm,bayar)
		print("-------- Menyimpan Data ---------\n")
		print()