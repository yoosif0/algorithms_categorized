"""
https://leetcode.com/problems/search-a-2d-matrix/
3/col1 = 3/4 = 0r3
4/4 = 1r0 = [1][0]
5/4 = 1r2 
#matrix

"""

import bisect
import unittest


class Solution:
    def searchMatrix(self, g: list[list[int]], t: int) -> bool:
        m = len(g)
        n = len(g[0])
        l = 0
        r = m * n
        while l < r:
            md = (r + l) // 2
            mv = g[md // n][md % n]
            if mv < t:
                l = md + 1
            else:
                r = md
        return l < m * n and g[l // n][l % n] == t


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True
        )
        self.assertEqual(
            t.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
            False,
        )
        self.assertEqual(
            t.searchMatrix([[1]], 1),
            True,
        )
        self.assertEqual(
            t.searchMatrix([[1, 1]], 0),
            False,
        )


if __name__ == "__main__":
    unittest.main()
