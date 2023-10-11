import unittest
import functools


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def countNumberOfNodes(node):
    if node is None:
        return 0
    return countNumberOfNodes(node.left) + countNumberOfNodes(node.right) + 1


class Tree():
    def __init__(self, root):
        self.root = root
    """
    If the expected index of any child node (2n+1 and 2n+2) (assuming it is represented in an array and assuming the tree is complete)
    is greater than the max possible index, it's not a complete tree
    """
    """
    This is the max possible index we can get if the tree is represented as an array
    """
    @functools.cached_property
    def totalNumberOfNodesInTree(self):
        return countNumberOfNodes(self.root) 

    def isCompleteRecurs(self, node, idealIndex):
        if node is None:
            return True
        if idealIndex >= self.totalNumberOfNodesInTree:
            return False
        return self.isCompleteRecurs(node.left, 2 * idealIndex + 1) and self.isCompleteRecurs(node.right, 2 * idealIndex + 2)
        
    def isComplete(self):
        return self.isCompleteRecurs(self.root, 0)


class TestCheckComplete(unittest.TestCase):
    def test_2_left(self):
        """
        Test that 2 branches with only left childs should fail
        --
                  17  
            2          3
         4     7      0    1  
        1     5
        [17,2,3,4,7,0,1,1,5]
        [0 ,1,2,3,4,5,6,7,8]
        """
        root = Node(17)
        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(7)

        root.right.left = Node(0)
        root.right.right = Node(1)

        root.left.left.left = Node(1)
        root.left.right.left = Node(5)
        t = Tree(root)
        result = t.isComplete()
        self.assertEqual(result, False)

    def test_perfect_tree(self):
        """
                  17  
            2          3
         4     7      0    1  
        """
        root = Node(17)
        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(7)

        root.right.left = Node(0)
        root.right.right = Node(1)
        t = Tree(root)
        result = t.isComplete()
        self.assertEqual(result, True)

    def test_one_side_perfect_tree(self):
        """
                  17  
            2          3
         4     7      0    1  
        1 5
        """
        root = Node(17)
        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(7)

        root.right.left = Node(0)
        root.right.right = Node(1)

        root.left.left.left = Node(1)
        root.left.left.right = Node(5)
        t = Tree(root)
        result = t.isComplete()
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()