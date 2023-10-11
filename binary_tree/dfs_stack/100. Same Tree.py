"""
https://leetcode.com/problems/same-tree/
"""
import unittest
from typing import Optional
from algoutils.tree_node import TreeNode


# def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#     if p is None or q is None:
#         return q is p
#     return (
#         self.isSameTree(p.left, q.left)
#         and self.isSameTree(p.right, q.right)
#         and p.val == q.val
#     )


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st = []
        st2 = []
        while p or q or st or st2:
            if bool(p) != bool(q) or bool(st) != bool(st2):
                return False
            if p:
                st.append(p)
                p = p.left
                st2.append(q)
                q = q.left
            else:
                p = st.pop()
                q = st2.pop()
                if p.val != q.val:
                    return False
                p = p.right
                q = q.right
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isSameTree(TreeNode(5), TreeNode(5)), True)


if __name__ == "__main__":
    unittest.main()
