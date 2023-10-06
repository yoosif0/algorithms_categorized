"""
https://leetcode.com/problems/house-robber-ii/
[30,      1,     5,      22,      60     ]
[[30,0], [1,30], [35,30],[52,35], [95,52]]

This is similar to max sum non adjacent but the difference is that the array represents a circle.
This means that the first and last elements are adjacent. That's why I solved once while excluding the first element
and another while excluding the last element. I returned back the max

#optimization
#incl_excl
#more_than_one_val_in_dp_cell
#circular
"""

import unittest


def rob1(a: list[int]) -> int:
    incl, excl = 0, 0
    for _, num in enumerate(a):
        incl, excl = num + excl, max(incl, excl)
    return max(excl, incl)


class Solution:
    def rob(self, a: list[int]) -> int:
        if len(a) == 1:
            return a[0]
        return max(rob1(a[1:]), rob1(a[0 : len(a) - 1]))


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.rob([30, 1, 5, 22, 60]), 65)
        self.assertEqual(t.rob([1]), 1)
        self.assertEqual(t.rob([1, 2]), 2)
        self.assertEqual(t.rob([1, 2, 1, 1]), 3)


if __name__ == "__main__":
    unittest.main()
