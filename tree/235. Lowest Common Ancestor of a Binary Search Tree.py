"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Note that this is a BST which means that the smaller value is always in the left and bigger 
value on the right. We just search for the first node that has a value greater than or equal 
one and less than or equal the other.
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p_tree: "TreeNode", s_tree: "TreeNode"
    ) -> "TreeNode":
        if p_tree.val < root.val and s_tree.val < root.val and root.left:
            return self.lowestCommonAncestor(root.left, p_tree, s_tree)
        if p_tree.val > root.val and s_tree.val > root.val and root.right:
            return self.lowestCommonAncestor(root.right, p_tree, s_tree)
        return root


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        child = TreeNode(1, TreeNode(0), TreeNode(2))
        child2 = TreeNode(4)
        tree = TreeNode(
            5,
            TreeNode(3, child, child2),
            TreeNode(7),
        )
        self.assertEqual(obj.lowestCommonAncestor(tree, child, child2).val, 3)
        child2 = TreeNode(4)
        child = TreeNode(2, TreeNode(1), child2)
        self.assertEqual(obj.lowestCommonAncestor(child, child, child2).val, 2)


if __name__ == "__main__":
    unittest.main()
