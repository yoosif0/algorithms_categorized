"""
https://leetcode.com/problems/rotate-array/
1, 2, 3, 4, 5, 6, 7
7  6  5  4  3  2  1
5  6  7  1  2  3  4
"""

from collections import deque
import unittest


def reverse(a: list[int], l: int, r: int):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1


class Solution:
    def rotate(self, a: list[int], k: int) -> None:
        k = k % len(a)
        reverse(a, 0, len(a) - 1)
        reverse(a, 0, k - 1)
        reverse(a, k, len(a) - 1)
        return a


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.rotate([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])
        self.assertEqual(obj.rotate([-1], 2), [-1])


if __name__ == "__main__":
    unittest.main()
