"""
https://leetcode.com/problems/maximum-subarray/
if num >w:
    reduce w
-2     1     -3    4   -1     2      1     -5    4
0      1      0    4    3     5      6      1    5

keep window unless it became negative, then reset it
"""


import sys
import unittest


class Solution:
    def maxSubArray(self, a: list[int]) -> int:
        w = 0
        bst = -sys.maxsize
        for r in range(len(a)):
            # shrink l directly
            if w < 0:
                w = 0
            w += a[r]
            bst = max(bst, w)
        return bst


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(t.maxSubArray([-1]), -1)
        self.assertEqual(t.maxSubArray([-2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
