jurusan_si = {
    "nama":"sistem informasi",
    "kaprodi":"Ulfi",
    "fakultas":"FTTI"
  }
mahasiswa1 = {
  "nama": "Agus Makmun",
  "nim": "650001",
  "jurusan":jurusan_si,
  "jumlah_saudara":4
}
mahasiswa2 = {
  "nama": "Siti Aminah",
  "nim": "650002",
  "jurusan":jurusan_si,
  "jumlah_saudara":2
}

for key,value in mahasiswa1.items():
  print(key,value)

# daftar_mahasiswa = [mahasiswa1,mahasiswa2]

# print(daftar_mahasiswa)
# print(type(daftar_mahasiswa))
# print(type(daftar_mahasiswa[0]))