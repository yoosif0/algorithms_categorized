class Node():
    left = None
    right = None
    def __init__(self, val):
        self.val = val


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, val):
        n = Node(val)
        if self.root is None:
            self.root = n 
            return
        self.recurInsert(n, self.root)

    def recurInsert(self, childNode, parentNode):
        if parentNode.left is None:
            parentNode.left = childNode
            return
        if parentNode.right is None:
            parentNode.right = childNode 
            return
        self.recurInsert(childNode, parentNode.left)

    def traverseInOrder(self):
        self.traverseInOrderRecurs(self.root)

    def traverseInOrderRecurs(self, node):
        if node.left is not None:
            self.traverseInOrderRecurs(node.left)
        print(node.val)
        if node.right is not None:
            self.traverseInOrderRecurs(node.right)



t = Tree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(1)
t.insert(1)
t.traverseInOrder()
