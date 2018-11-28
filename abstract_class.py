from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    def do_public_method(self):
      print ("This is a public method")

    ''' contoh abstract method '''
    @abstractmethod
    def do_something(self):
        pass

class ImplementationAbstractExample(AbstractClassExample):
  ''' method ini wajib diimplementasikan, karena di 
    AbstractClassExample.do_something() dideklarasikan 
    sebagai abstract method
  '''
  def do_something(self):
    return self.value+2

a = ImplementationAbstractExample(2)
a.do_public_method()
print(a.do_something())















# class AbstractClassExample2(AbstractClassExample):
 
#     def __init__(self, value):
#         self.value = value
#         super().__init__()
    
#     @abstractmethod
#     def do_another_something(self):
#         pass

# a = AbstractClassExample2()