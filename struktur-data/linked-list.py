class Node:
  def __init__(self,data):
    self.dataval = data
    self.next = None

head = None

# menambahkan node di depan
def addFirst(node):
  global head
  node.next = head 
  head = node

# menambahkan node di ujung
def addLast(node):
  global head
  ujung = head 
  while ujung.next:
    ujung = ujung.next
  ujung.next = nodeakhir

# menyispkan node di tengah / setelah node awal
def insertAt(nodeAwal,nodebaru):
  global head
  nodebaru.next = nodeAwal.next 
  nodeAwal.next = nodebaru

def deleteNode(nodeHapus):
  global head
  node = head
  if nodeHapus == node:
    # jika yang dihapus node pertama
    head = nodeHapus.next
  else:
    while not node.next == nodeHapus:
      node = node.next

    node.next = nodeHapus.next

def printNode():
  global head
  node = head
  print("----- print node ----")
  while node  is not None:
    print(node.dataval)
    node = node.next


node1 = Node("node 1")
addFirst(node1)
printNode()

node2  = Node("node 2")
addFirst(node2)
printNode()

nodeakhir = Node("akhir")
addLast(nodeakhir)
printNode()

nodebaru = Node("Baru")
insertAt(node1,nodebaru)
printNode()

deleteNode(node2)
printNode()