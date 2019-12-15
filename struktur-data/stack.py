class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self): 
    return self.items == []
  def push(self, item): 
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items)-1]
  def size(self):
    return len(self.items)


s = Stack()

print(s.isEmpty())
s.push("A")
s.push("B")

print(s.items)
print(s.pop())
print(s.items)










# queue dg lib  python
from pythonds.basic.stack import Stack
s=Stack()
print(s.isEmpty())
s.push(4) 
s.push('dog') 
print(s.peek())
s.push(True) 
print(s.size()) 
print(s.isEmpty())


# memeriksa tanda kurung
from pythonds.basic.stack import Stack
def parChecker(symbolString): 
  s = Stack()
  balanced = True
  index = 0
  while index < len(symbolString) and balanced: 
    symbol = symbolString[index]
    if symbol == "(":
      s.push(symbol) 
    else:
      if s.isEmpty(): 
        balanced = False
      else: 
        s.pop()
    index = index + 1

    if balanced and s.isEmpty(): 
      return True
    else:
      return False

print(parChecker('((()))')) 
print(parChecker('(()'))
