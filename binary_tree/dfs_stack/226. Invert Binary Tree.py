"""
https://leetcode.com/problems/invert-binary-tree/
"""

import unittest
from typing import Optional
from algoutils.tree_node import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        inverted = obj.invertTree(None)
        self.assertIsNone(inverted)
        inverted = obj.invertTree(TreeNode(5))
        self.assertIsNotNone(inverted)


if __name__ == "__main__":
    unittest.main()
