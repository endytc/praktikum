class SuperInduk():
  def m(self):
    print ("call method m from SuperInduk")

class SuperInduk2():
  def m(self):
    print ("call method m from SuperInduk2")

class Induk1(SuperInduk):
  def m(self):
    print ("call method m from Induk1")

class Induk2(SuperInduk):
  def m(self):
    print ("call method m from Induk2")

class Anak(Induk1,Induk2):
  pass

a = Anak()
a.m()
help(a)