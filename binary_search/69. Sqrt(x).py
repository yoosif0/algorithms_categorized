"""
@nested-tags:binary_search/no_arr,binary_search/remove_from_r
https://leetcode.com/problems/sqrtx
"""

import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l < r:
            mid = (l + r + 1) // 2
            if mid * mid > x:
                r = mid - 1
            else:
                l = mid
        return r


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.mySqrt(8), 2)
        self.assertEqual(t.mySqrt(4), 2)


if __name__ == "__main__":
    unittest.main()
