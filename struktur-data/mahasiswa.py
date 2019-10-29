mahasiswa_list = set({})

i = 0
while i<2:
  nim = raw_input("NIM: ")
  nama = raw_input("Nama: ")
  jumlah_saudara = input("Jumlah Saudara: ")
  mahasiswa = {
    "nim": nim,
    "nama": nama,
    "jumlah_saudara":jumlah_saudara
  }
  mahasiswa_list.add(mahasiswa)
  i += 1

print(mahasiswa_list)