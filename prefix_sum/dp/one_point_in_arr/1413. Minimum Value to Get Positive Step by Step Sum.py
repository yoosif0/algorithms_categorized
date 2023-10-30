"""
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
We need to let the whole prefix sum arr positive so we just identify the lowest spot and make sure 
the starting element will cover it's negativity
"""
from itertools import accumulate
import unittest


class Solution:
    def minStartValue(self, a: list[int]) -> int:
        ans = min(list(accumulate(a, initial=0)))
        # the start value should be positive (hence the "max")
        return max(-ans + 1, 1)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minStartValue([-3, 2, -3, 4, 2]), 5)
        self.assertEqual(t.minStartValue([1, 2]), 1)
        self.assertEqual(t.minStartValue([1, -2, -3]), 5)


if __name__ == "__main__":
    unittest.main()
