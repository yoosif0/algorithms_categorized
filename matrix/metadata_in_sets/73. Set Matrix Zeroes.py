"""
https://leetcode.com/problems/set-matrix-zeroes/
#set
"""

import unittest


class Solution:
    def setZeroes(self, grid: list[list[int]]) -> None:
        rows = set()
        columns = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    rows.add(i)
                    columns.add(j)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if i in rows or j in columns:
                    grid[i][j] = 0


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        )
        self.assertEqual(
            t.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]),
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        )


if __name__ == "__main__":
    unittest.main()
