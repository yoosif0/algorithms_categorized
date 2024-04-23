"""
https://leetcode.com/problems/can-place-flowers
"""

import unittest


class Solution:
    def canPlaceFlowers(self, a: list[int], n: int) -> bool:
        if len(a) == 1:
            if a[0] == 0:
                n -= 1
            return n <= 0
        if a[0] == 0 and a[1] == 0:
            a[0] = 1
            n -= 1
        for i in range(1, len(a) - 1):
            if a[i - 1] == 0 and a[i] == 0 and a[i + 1] == 0:
                a[i] = 1
                n -= 1
        if a[-1] == 0 and a[-2] == 0:
            n -= 1
        return n <= 0


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.canPlaceFlowers([1, 0, 0, 0, 1], 1), True)
        self.assertEqual(obj.canPlaceFlowers([1, 0, 0, 0, 1], 2), False)
        self.assertEqual(obj.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2), False)
        self.assertEqual(obj.canPlaceFlowers([1], 1), False)


if __name__ == "__main__":
    unittest.main()
