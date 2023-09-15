"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""
import sys
import unittest
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root: Optional[TreeNode], threshold: int):
            nonlocal ans
            if not root:
                return
            if root.val >= threshold:
                ans += 1
            new_min_allowed = max(root.val, threshold)
            dfs(root.left, new_min_allowed)
            dfs(root.right, new_min_allowed)

        dfs(root, -sys.maxsize)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(4, TreeNode(5), TreeNode(6)), TreeNode(7)),
            TreeNode(3, TreeNode(2)),
        )
        self.assertEqual(obj.goodNodes(tree), 7)


if __name__ == "__main__":
    unittest.main()
