"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

import sys
import unittest
from typing import Optional
from algoutils.tree_node import TreeNode


class Solution:
    def isValidBST(
        self,
        root: Optional[TreeNode],
        upper_limit=sys.maxsize,
        bottom_limit=-sys.maxsize,
    ) -> bool:
        if not root:
            return True
        return (
            root.val < upper_limit
            and root.val > bottom_limit
            and self.isValidBST(root.left, root.val, bottom_limit)
            and self.isValidBST(root.right, upper_limit, root.val)
        )


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        tree = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(obj.isValidBST(tree), True)
        tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertEqual(obj.isValidBST(tree), False)


if __name__ == "__main__":
    unittest.main()
