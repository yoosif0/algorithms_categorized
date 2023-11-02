"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""

import unittest


class Solution:
    def maxProfit(self, a: list[int]) -> int:
        bst = 0
        l = 0
        for r in range(1, len(a)):
            if a[r] < a[l]:
                l = r
            else:
                bst = max(bst, a[r] - a[l])
        return bst


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxProfit([7, 1, 5, 3, 6, 4]), 5)


if __name__ == "__main__":
    unittest.main()
