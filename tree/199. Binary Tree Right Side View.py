"""
https://leetcode.com/problems/binary-tree-right-side-view/
This is very similar to 102. Binary Tree Level Order Traversal.

The difference here is that we pick the right most number in each level_arr in the visited arr
"""

from collections import deque
import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        visited = []
        q: deque[tuple[Optional[TreeNode], int]] = deque([])
        if root:
            q.append((root, 0))
        while len(q) > 0:
            (node, level) = q.popleft()
            if not node:
                continue
            if level == len(visited):
                visited.append([])
            visited[level].append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        ans = []
        for level_arr in visited:
            if level_arr:
                ans.append(level_arr[-1])
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        tree = TreeNode(
            1,
            TreeNode(3, TreeNode(50)),
            TreeNode(2, TreeNode(4, TreeNode(5), TreeNode(6)), TreeNode(7)),
        )
        self.assertEqual(obj.rightSideView(tree), [1, 2, 7, 6])
        # tree = TreeNode(1, TreeNode(3, TreeNode(50)), None)
        # self.assertEqual(obj.rightSideView(tree), [1, 3, 50])


if __name__ == "__main__":
    unittest.main()
