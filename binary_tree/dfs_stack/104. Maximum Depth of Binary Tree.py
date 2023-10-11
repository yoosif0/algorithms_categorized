"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

         1
       2    3
      4 5  6  7
         8
"""

import unittest
from typing import Optional
from algoutils.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.maxDepth(TreeNode(5)), 1)
        self.assertEqual(obj.maxDepth(TreeNode(5, TreeNode(1))), 2)


if __name__ == "__main__":
    unittest.main()
