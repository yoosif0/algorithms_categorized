"""
https://leetcode.com/problems/sort-colors/
1220120102120110100010
lm                   r
"""

import unittest


class Solution:
    def sortColors(self, a: list[int]) -> None:
        l = m = 0
        r = len(a) - 1
        while m <= r:
            if a[m] == 1:
                m += 1
            elif a[m] == 0:
                a[m], a[l] = a[l], a[m]
                m += 1
                l += 1
            else:
                a[m], a[r] = a[r], a[m]
                r -= 1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        t.sortColors([2, 0, 2, 1, 1, 0])
        t.sortColors(
            [0, 0, 0, 2, 0, 0, 1, 0, 2, 0, 2, 2, 1, 0, 0, 0, 2, 0, 2, 1, 1, 0, 2, 1]
        )


if __name__ == "__main__":
    unittest.main()
