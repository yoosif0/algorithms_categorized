"""
https://leetcode.com/problems/house-robber-iii

l_max_incl:6
l_max_excl:2
r_max_incl:4
r_max_excl:3

#optimization
#incl_excl
#more_than_one_val_in_dp_cell
#tree
#dfs
#optimal_substructure
#overlapping_subproblems
#recursion
#remove_overlapping_subproblems
#remove_overlapping_subproblems_by_returning_more_values
"""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(x: Optional[TreeNode]):
    if not x:
        return [0, 0]
    right = dfs(x.right)
    left = dfs(x.left)
    incl = x.val + left[1] + right[1]
    excl = max(left[0], left[1]) + max(right[0], right[1])
    return [incl, excl]


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = dfs(root)
        return max(res[0], res[1])


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        two = TreeNode(2, None, TreeNode(3))
        three = TreeNode(3, None, TreeNode(1))
        tree = TreeNode(3, two, three)
        self.assertEqual(t.rob(tree), 7)
        fo = TreeNode(4, TreeNode(1), TreeNode(3))
        fve = TreeNode(5, None, TreeNode(1))
        tree = TreeNode(3, fo, fve)
        self.assertEqual(t.rob(tree), 9)


if __name__ == "__main__":
    unittest.main()
