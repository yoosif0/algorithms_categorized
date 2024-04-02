"""
https://leetcode.com/problems/longest-continuous-increasing-subsequence
"""

import unittest


class Solution:
    def findLengthOfLCIS(self, a: list[int]) -> int:
        cur = 1
        bst = cur
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                cur += 1
                bst = max(cur, bst)
            else:
                cur = 1
        return bst


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.findLengthOfLCIS([1, 3, 5, 4, 7]), 3)
        self.assertEqual(t.findLengthOfLCIS([2, 2, 2, 2, 2]), 1)


if __name__ == "__main__":
    unittest.main()
