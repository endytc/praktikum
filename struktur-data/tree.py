class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                # jika node kiri NULL, buat node di kiri
                if self.left is None:
                    self.left = Node(data)
                else:
                    # jika node kiri sudah terisi, lanjutkan pencarian
                    # sampai ditemukan posisi yang sesuai
                    self.left.insert(data)
            elif data > self.data:
                # jika node kanan NULL, buat node di kanan
                if self.right is None:
                    self.right = Node(data)
                else:
                    # jika node kanan sudah terisi, lanjutkan pencarian
                    # sampai ditemukan posisi yang sesuai
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def preorder(self,node):
      if node == None:
        return
      print(node.data)
      self.preorder(node.left)
      self.preorder(node.right)
      


root = Node(5)
root.insert(3)
root.insert(7)
root.insert(1)
root.insert(4)
root.insert(6)
print(root.findval(7))
print(root.findval(14))

root.preorder(root)