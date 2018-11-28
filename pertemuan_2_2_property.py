class barang():
    def __init__(self,produk,qty,harga):
        self.produk = produk
        self.qty = qty
        self.harga = harga

class penjualan():
    def __init__(self,no_nota,konsumen):
        self.no_nota = no_nota
        self.konsumen = konsumen
        self._daftar_keranjang = list()
    @staticmethod
    def toko(self):
        self.no_nota
        return "Toko Suka Maju"
    @property
    def details(self):
        return self._daftar_keranjang

    @details.setter
    def details(self,barang):
        self._daftar_keranjang.append(barang)
        pass
    
    @details.delter
    def details(self):
        removed= self._daftar_keranjang.pop(-1)

    def total(self):
        total = 0
        for x in self._daftar_keranjang:
            total += x.harga
        return total
