class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def isFullRecurs(self, node):
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self.isFullRecurs(node.left) and self.isFullRecurs(node.right)
        return False

    def isFull(self):
        return self.isFullRecurs(self.root)

t = Tree()
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.right.left = Node(1)
# t.root.right.right = Node(4)
# t.root.left.left.left = Node(5)
print(t.isFull())
