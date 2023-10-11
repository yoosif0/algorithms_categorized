"""
https://leetcode.com/problems/validate-binary-search-tree/
"""

import sys
import unittest
from typing import Optional
from algoutils.tree_node import TreeNode

# class Solution:
#     def isValidBST(
#         self,
#         root: Optional[TreeNode],
#         upper_limit=sys.maxsize,
#         bottom_limit=-sys.maxsize,
#     ) -> bool:
#         if not root:
#             return True
#         return (
#             root.val < upper_limit
#             and root.val > bottom_limit
#             and self.isValidBST(root.left, root.val, bottom_limit)
#             and self.isValidBST(root.right, upper_limit, root.val)
#         )


class Solution:
    def isValidBST(self, tn: Optional[TreeNode]) -> bool:
        st = []
        ctx = -sys.maxsize
        while st or tn:
            if tn:
                st.append(tn)
                tn = tn.left
            else:
                tn = st.pop()
                if tn.val <= ctx:
                    return False
                ctx = tn.val
                tn = tn.right
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))), True)
        self.assertEqual(
            obj.isValidBST(
                TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()
