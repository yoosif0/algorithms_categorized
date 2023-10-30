"""
https://leetcode.com/problems/range-sum-query-immutable/
-2, 0, 3, -5, 2, -1
0,-2,0,1, -4, -2,-3
"""
from itertools import accumulate
import unittest


class NumArray:
    def __init__(self, a: list[int]):
        self.dp = list(accumulate(a, initial=0))

    def sumRange(self, l: int, r: int) -> int:
        return self.dp[r + 1] - self.dp[l]


class Test(unittest.TestCase):
    def test(self):
        t = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(t.sumRange(0, 2), 1)


if __name__ == "__main__":
    unittest.main()
