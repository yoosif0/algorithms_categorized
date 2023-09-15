"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
