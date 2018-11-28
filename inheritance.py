class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    
    def m(self):
      print("m of D called")
    
    @property
    def A(self):
      return A
d = D()
d.A.m(d)