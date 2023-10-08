"""
https://leetcode.com/problems/subtree-of-another-tree/
"""

import unittest
from typing import Optional
from hashlib import sha256
from algoutils.tree_node import TreeNode


class FoundSubtree(Exception):
    pass


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def hashNodeWithSideEffect(root: Optional[TreeNode], doComparison: bool):
            if root is None:
                return "#"
            m = sha256()
            m.update(str(root.val).encode())
            m.update(hashNodeWithSideEffect(root.left, doComparison).encode())
            m.update(hashNodeWithSideEffect(root.right, doComparison).encode())
            hex_digest = m.hexdigest()
            if doComparison and hex_digest == subRootHash:
                raise FoundSubtree()
            return hex_digest

        subRootHash = hashNodeWithSideEffect(subRoot, False)
        try:
            hashNodeWithSideEffect(root, True)
            return False
        except FoundSubtree:
            return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.isSubtree(TreeNode(5, TreeNode(5)), TreeNode(5, TreeNode(5))), True
        )
        self.assertEqual(
            obj.isSubtree(TreeNode(3, TreeNode(5)), TreeNode(5, TreeNode(5))), False
        )


if __name__ == "__main__":
    unittest.main()
