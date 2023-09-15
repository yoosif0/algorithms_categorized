import unittest

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST():
    def __init__(self, root):
        self.root = root

    def insertRecurs(self, node, val):
        if val == node.val:
            raise ValueError("same value exists")
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
                return
            self.insertRecurs(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
                return
            self.insertRecurs(node.right, val)

    def deleteRecurs(self, node, val):
        if val < node.val:
            if node.left is not None and node.left.val == val:
                node.left = None
                return
            self.deleteRecurs(node.left, val)
        else:
            if node.right is not None and node.right.val == val:
                node.right = None
                return
            self.deleteRecurs(node.right, val)

    def findRecurs(self, node, val):
        if val == node.val:
            return True
        if val < node.val and node.left is not None:
            return self.findRecurs(node.left, val)
        if val > node.val and node.right is not None:
            return self.findRecurs(node.right, val)
        return False
    
    def insert(self, val):
       self.insertRecurs(self.root, val) 
     
    def find(self, val):
       return self.findRecurs(self.root, val)   

    def delete(self, val):
       return self.deleteRecurs(self.root, val)   
    

class TestBST(unittest.TestCase):
    def test_insert_and_find(self):
        """
                     17
          5                            50
           10
        """
        root = Node(17)
        t = BST(root)
        t.insert(5)
        t.insert(50)
        t.insert(10)
        self.assertEqual(t.root.right.val, 50)
        self.assertEqual(t.root.left.val, 5)
        self.assertEqual(t.root.left.right.val, 10)
        self.assertEqual(t.find(17), True)
        self.assertEqual(t.find(5), True)
        self.assertEqual(t.find(10), True)
        self.assertEqual(t.find(50), True)
        t.delete(10)
        self.assertEqual(t.find(10), False)


    def test_delete_non_leaf(self):
        """
                     17
             5                            50
        3        10
               6    7
        We should be able to find children like "10" when we delete a parent like "5"
        """
        root = Node(17)
        t = BST(root)
        t.insert(5)
        t.insert(50)
        t.insert(10)
        t.insert(3)
        t.delete(5)
        self.assertEqual(t.find(10), True)


if __name__ == '__main__':
    unittest.main()