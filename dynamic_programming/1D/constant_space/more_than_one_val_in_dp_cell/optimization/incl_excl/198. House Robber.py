"""
https://leetcode.com/problems/house-robber/
[2,      7,    9,      3,      1,     20,    5,22,60]
[[2,0],[7,2],[11,7],[10,11],[12,11],[31,12],[17,31]]
9:it's best to take 9 and 2 and max=11
3:3 it's best to take 9 and 2 too
[2,7,11,10,12,30,17,42,]

#optimization
#more_than_one_val_in_dp_cell
#incl_excl
"""

import unittest


class Solution:
    def rob(self, a: list[int]) -> int:
        inc, exc = 0, 0
        for i in range(len(a)):
            inc, exc = a[i] + exc, max(inc, exc)
        return max(exc, inc)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.rob([2, 7, 9, 3, 1, 20, 5, 22, 60]), 91)


if __name__ == "__main__":
    unittest.main()
