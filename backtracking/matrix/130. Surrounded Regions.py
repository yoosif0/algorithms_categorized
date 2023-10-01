"""
https://leetcode.com/problems/surrounded-regions/
#boundary

1.Move through all 4 boundaries and if any O exists, dfs and fill it with # (something that means
that this have access to outside world and that this O should stay an O and not X). 
2.Now, any O left should be converted to X. Go through all O and convert them to X and convert # to O
"""

import unittest


class Solution:
    def solve(self, grid: list[list[str]]) -> None:
        g_len = len(grid)
        r_len = len(grid[0])

        def dfs(r: int, c: int):
            if not 0 <= r < g_len or not 0 <= c < r_len or grid[r][c] != "O":
                return
            # these are the ones that should stay "O"
            grid[r][c] = "c"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Move through all 4 boundaries
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                at_border = i == 0 or i == g_len - 1 or j == 0 or j == r_len - 1
                if at_border and grid[i][j] == "0":
                    dfs(i, j)

        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                if grid[i][j] == "c":
                    grid[i][j] = "O"


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # t.solve(
        #     [
        #         ["X", "X", "X", "X"],
        #         ["X", "O", "O", "X"],
        #         ["X", "X", "O", "X"],
        #         ["X", "O", "X", "X"],
        #     ]
        # )
        t.solve([["O", "O"], ["O", "O"]])


if __name__ == "__main__":
    unittest.main()
