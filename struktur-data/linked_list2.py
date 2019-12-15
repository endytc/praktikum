class Node:
  def __init__(self, data):
    self.dataval = data
    self.next = None
    self.previous = None

node1 = Node("node 1")
head  = node1 

# print(node1.dataval)
# print(node1.next)

node2 = Node("node 2")
node2.next = head
head = node2

print(node2.dataval)
print(node2.next.dataval)

print(node1.dataval)
print(node1.next.dataval if node1.next else "None")

i = 0
node = head
while node is not None:
  print("loop %s node: %s" % (i, node.dataval))
  node = node.next
  i += 1

