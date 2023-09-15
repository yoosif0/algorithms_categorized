class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class NotPerfect(Exception):
    pass


class Tree():
    def __init__(self):
        self.root = None

    def getHeightAndThrowIfNotFull(self, node):
        if node.left is None and node.right is None:
            return 0
        if node.left is not None and node.right is None:
            raise NotPerfect()
        if node.left is None and node.right is not None:
            raise NotPerfect()
        l = self.getHeightAndThrowIfNotFull(node.left) 
        r = self.getHeightAndThrowIfNotFull(node.right)
        if r != l:
            raise NotPerfect()
        return r + 1

    def isPerfect(self):
        try:
            self.getHeightAndThrowIfNotFull(self.root)
            return True
        except NotPerfect:
            return False

t = Tree()
t.root = Node(1)
t.root.right = Node(3)
t.root.right.left = Node(1)
t.root.right.right = Node(4)
t.root.left = Node(2)
t.root.left.left = Node(5)
t.root.left.right = Node(5)
print(t.isPerfect())