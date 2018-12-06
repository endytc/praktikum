from abc import ABCMeta, abstractmethod, ABC

class Transaksi(ABC):
  @abstractmethod
  def tagihan(self): pass
  @abstractmethod
  def pembayaran(self): pass

class Penjualan(Transaksi):
  def tagihan(self):
    print("tagihan penjualan")
  def pembayaran(self):
    print("pembayran penjualan")

class Pembelian(Transaksi):
  def tagihan(self):
    print("tagihan pembelian")
  def pembayaran(self):
    print("pembayaran pembelian")

a = Pembelian()
a.pembayaran()