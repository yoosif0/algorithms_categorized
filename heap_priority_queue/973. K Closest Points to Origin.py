"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""

import math
import unittest


class Solution:
    def kClosest(self, a: list[list[int]], k: int) -> list[list[int]]:
        # sort by distance equation
        a.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return a[:k]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertEqual(obj.kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])


if __name__ == "__main__":
    unittest.main()
