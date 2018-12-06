class produk():
    def __init__(self,produk,qty,harga):
        self.produk = produk
        self.qty = qty
        self.harga = harga
    def subTotal(self):
      if( self.qty >= 5):
        harga = self.harga * self.qty - (self.harga * self.qty * 10/100)
      else:
        harga = self.harga * self.qty
      return harga
class penjualan():
    def __init__(self,no_nota,konsumen):
        self.no_nota = no_nota
        self.konsumen = konsumen
        self.keranjang = list()
    def addProduk(self,produk):
        self. keranjang.append(produk)
        pass
    def tagihan(self):
        total = 0
        for x in self. keranjang:
          if( x.qty >= 5):
            total += (x.harga * x.qty * (100-10)/100)
          else:
            total += x.harga * x.qty
        return total
    def print(self):
        for x in self.keranjang:
          if( x.qty >= 5):
            print("{} Diskon {} Harga {} Total {}".format(x.produk,
              (x.harga * x.qty * 10/100),x.harga,x.subTotal()))
          else:
            print("{} Harga {} Total {}".format(x.produk,x.harga,
              x.subTotal()))

sabun = produk("Sabun XXX",10,2000)
rinso = produk("Pewangi Ruangan ABC",2,20000)
jual = penjualan("0001","Afka")
jual.addProduk(sabun)
jual.addProduk(rinso)
print("Tagihan %s" % (jual.tagihan ()))
jual.print()
