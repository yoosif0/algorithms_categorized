class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class NotBalanced(Exception):
    pass

class Tree():
    def __init__(self):
        self.root = None

    def getHeightThrowIfUnBalanced(self, node):
        if node is None:
            return 0
        lHeight = self.getHeightThrowIfUnBalanced(node.left)
        rHeight = self.getHeightThrowIfUnBalanced(node.right) 
        if abs(lHeight - rHeight) > 1:
            raise NotBalanced()
        return max(lHeight, rHeight) + 1

    def isBalanced(self):
        try:
            self.getHeightThrowIfUnBalanced(self.root)
            return True
        except NotBalanced:
            return False

t = Tree()
t.root = Node(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.right.left = Node(1)
t.root.left.left = Node(4)
t.root.left.left.left = Node(5)
print(t.isBalanced())

#     1  
#   2   3
# 4    1  
#5          
