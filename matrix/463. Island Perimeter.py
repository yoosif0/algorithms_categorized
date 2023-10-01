"""
https://leetcode.com/problems/island-perimeter/
each cell has at most a perimeter of 3 and min of 0. 3 when it's connect to one cell and 0
when connected in all 4 sides
#traversal #graph #search 
"""

import unittest


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        g_len = len(grid)
        r_len = len(grid[0])
        ans = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if not cell:
                    continue
                peri = 4
                neighbors = [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
                for c in neighbors:
                    r_i = c[0]
                    c_i = c[1]
                    if r_i >= g_len or c_i >= r_len or r_i < 0 or c_i < 0:
                        continue
                    # if a neighbor exists from a side then reduce the peri by 1
                    if grid[r_i][c_i]:
                        peri -= 1
                ans += peri
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]),
            16,
        )


if __name__ == "__main__":
    unittest.main()
