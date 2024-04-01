"""
https://leetcode.com/problems/longest-harmonious-subsequence
"""

import collections
import unittest


class Solution:
    def findLHS(self, a: list[int]) -> int:
        m = collections.Counter(a)
        bst = 0
        for k in m:
            # update bst only if the number following it exists
            nxt = m[k + 1]
            if nxt:
                bst = max(bst, m[k] + nxt)
        return bst


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.findLHS([1, 3, 2, 2, 5, 2, 3, 7]), 5)
        self.assertEqual(obj.findLHS([1, 2, 3, 4]), 2)
        self.assertEqual(obj.findLHS([1, 1, 1, 1]), 0)
        self.assertEqual(obj.findLHS([1, 4, 1, 3, 1, -14, 1, -13]), 2)


if __name__ == "__main__":
    unittest.main()
