"""
https://leetcode.com/problems/sqrtx
"""

import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l < r:
            m = (l + r + 1) // 2
            if m * m > x:
                r = m - 1
            else:
                l = m
        return r


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.mySqrt(8), 2)
        self.assertEqual(t.mySqrt(4), 2)


if __name__ == "__main__":
    unittest.main()
