"""
https://leetcode.com/problems/flood-fill/
check 4 neighbors. if color is dfferent, continue, otherwise mark that it should be filled.
check the 4 neighbors for it too.
"""

import unittest


class Solution:
    def floodFill(
        self, grid: list[list[int]], sr: int, sc: int, new_color: int
    ) -> list[list[int]]:
        old_color = grid[sr][sc]
        if old_color == new_color:
            return grid
        g_len = len(grid)
        r_len = len(grid[0])

        def dfs(r: int, c: int):
            if not 0 <= r < g_len or not 0 <= c < r_len or grid[r][c] != old_color:
                return
            grid[r][c] = new_color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return grid


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        )


if __name__ == "__main__":
    unittest.main()
