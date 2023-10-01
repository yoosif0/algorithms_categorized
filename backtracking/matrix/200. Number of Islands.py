"""
https://leetcode.com/problems/number-of-islands/
#set
#mark_visited
#in_place_mark_visited
#return_null
#for_loop_reading_from_updated_grid

The grid in the for is different from one iteration to another since the dfs change 
the grid in place
"""
import unittest


class Solution:
    def numIslands(self, grid: list[list[int]]) -> int:
        g_len = len(grid)
        r_len = len(grid[0])
        ans = 0

        def dfs(r: int, c: int):
            if not 0 <= r < g_len or not 0 <= c < r_len or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1

        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.numIslands(
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ),
            1,
        )
        self.assertEqual(
            t.numIslands(
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
