"""
https://leetcode.com/problems/balanced-binary-tree/
get depth of left and right and check if there is no more difference than one

"""

import unittest
from typing import Optional
from algoutils.tree_node import TreeNode


class NotBalancedError(Exception):
    pass


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepthWithSideEffect(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            l = maxDepthWithSideEffect(root.left)
            r = maxDepthWithSideEffect(root.right)
            if abs(l - r) > 1:
                raise NotBalancedError()
            return 1 + max(l, r)

        try:
            maxDepthWithSideEffect(root)
            return True
        except NotBalancedError:
            return False


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isBalanced(TreeNode(5)), True)
        self.assertEqual(obj.isBalanced(TreeNode(5, TreeNode(1))), True)
        self.assertEqual(obj.isBalanced(TreeNode(5, TreeNode(1), TreeNode(6))), True)
        tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(obj.isBalanced(tree), True)
        tree = TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
            TreeNode(2),
        )
        self.assertEqual(obj.isBalanced(tree), False)


if __name__ == "__main__":
    unittest.main()
