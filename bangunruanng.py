class balok():
  def __init__(self,panjang,lebar,tinggi):
    self.panjang = panjang
    self.lebar = lebar
    self.tinggi = tinggi
  
  def luas(self):
    return 2*(self.panjang*self.lebar+self.lebar*self.tinggi+self.panjang*self.tinggi)
  
  def volume(self):
    return self.panjang*self.lebar*self.tinggi

class bola():
  def __init__(self,jari2):
    self.phi = 22/7
    self.r = jari2
  def luas(self):
    return (4)*self.phi*self.r**2
  def volume(self):
    return (4/3)*self.phi*self.r**3


b = balok(2,3,5)
print(b.luas())
print(b.volume())

b2 = balok(6,2,5)
print(b2.luas())
print(b2.volume())

bola = bola(8)
print(bola.luas())
print(bola.volume())