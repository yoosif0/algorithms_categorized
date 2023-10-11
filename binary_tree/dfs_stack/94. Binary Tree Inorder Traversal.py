"""
https://leetcode.com/problems/binary-tree-inorder-traversal
#dfs_stack
"""
import unittest
from typing import Optional
from algoutils.tree_node import TreeNode


# stack
class Solution:
    def inorderTraversal(self, tn: Optional[TreeNode]) -> list[int]:
        ans = []
        st = []
        while st or tn:
            if tn:
                st.append(tn)
                tn = tn.left
            else:
                tn = st.pop()
                ans.append(tn.val)
                tn = tn.right
        return ans


# recursive dfs
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
#         ans = []

#         def dfs(n):
#             if not n:
#                 return
#             dfs(n.left)
#             ans.append(n.val)
#             dfs(n.right)

#         dfs(root)
#         return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        th = TreeNode(3, None, None)
        tw = TreeNode(2, th, None)
        on = TreeNode(1, None, tw)
        self.assertEqual(obj.inorderTraversal(on), [1, 3, 2])


if __name__ == "__main__":
    unittest.main()
