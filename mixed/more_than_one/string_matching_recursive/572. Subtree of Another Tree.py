"""
@nested-tags/matching,binary_tree/dfs
https://leetcode.com/problems/subtree-of-another-tree/
"""

import unittest
from typing import Optional
from algoutils.tree_node import TreeNode
from hashlib import sha256


class Solution:
    def traverse(self, node: Optional[TreeNode]):
        if node:
            return f"#{node.val} {self.traverse(node.left)} {self.traverse(node.right)}"
        return "n"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.traverse(subRoot) in self.traverse(root)


class FoundSubtree(Exception):
    pass

class SolutionRecursive:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def hh(root: Optional[TreeNode], doComparison: bool):
            if root is None:
                return "#"
            m = sha256()
            m.update(str(root.val).encode())
            m.update(hh(root.left, doComparison).encode())
            m.update(hh(root.right, doComparison).encode())
            hd = m.hexdigest()
            if doComparison and hd == srh:
                raise FoundSubtree()
            return hd

        srh = hh(subRoot, False)
        try:
            hh(root, True)
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
