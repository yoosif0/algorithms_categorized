"""
https://leetcode.com/problems/same-tree/
"""
import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     arr = []

    #     def dfs(root: Optional[TreeNode]) -> None:
    #         if root is None:
    #             arr.append(None)
    #             return
    #         arr.append(root.val)
    #         dfs(root.left)
    #         dfs(root.right)

    #     dfs(p)
    #     p_arr = arr
    #     arr = []
    #     dfs(q)
    #     return p_arr == arr

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return q is p
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
            and p.val == q.val
        )


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isSameTree(TreeNode(5), TreeNode(5)), True)


if __name__ == "__main__":
    unittest.main()
