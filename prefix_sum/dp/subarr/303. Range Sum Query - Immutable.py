"""
https://leetcode.com/problems/range-sum-query-immutable/
-2, 0, 3, -5, 2, -1
0,-2,0,1, -4, -2,-3
"""
import unittest


class NumArray:
    def __init__(self, a: list[int]):
        dp = [0 for _ in range(len(a) + 1)]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + a[i - 1]
        self.dp = dp

    def sumRange(self, l: int, r: int) -> int:
        return self.dp[r + 1] - self.dp[l]


class Test(unittest.TestCase):
    def test(self):
        t = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(t.sumRange(0, 2), 1)


if __name__ == "__main__":
    unittest.main()
