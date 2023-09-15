"""
https://leetcode.com/problems/diameter-of-binary-tree/

To get the max path length from right to left, you add max_depth of right to max_depth of left.
The issue here is that you want to get the diameter (which is max path length for the parent node 
or any child). Since a child might have a longer path from left to right than root so you need to 
have side effect and keep track of max length.
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def maxDepthWithPathLengthSideEffect(root: Optional[TreeNode]) -> int:
            nonlocal ans
            if root is None:
                return 0
            l = maxDepthWithPathLengthSideEffect(root.left)
            r = maxDepthWithPathLengthSideEffect(root.right)
            # path from left to right for current node
            current_max_path_length = l + r
            ans = max(current_max_path_length, ans)
            return 1 + max(l, r)

        maxDepthWithPathLengthSideEffect(root)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.diameterOfBinaryTree(TreeNode(5)), 0)
        self.assertEqual(obj.diameterOfBinaryTree(TreeNode(5, TreeNode(1))), 1)
        self.assertEqual(
            obj.diameterOfBinaryTree(TreeNode(5, TreeNode(1), TreeNode(6))), 2
        )
        tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(obj.diameterOfBinaryTree(tree), 3)


if __name__ == "__main__":
    unittest.main()
