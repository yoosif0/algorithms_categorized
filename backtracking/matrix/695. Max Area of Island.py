"""
https://leetcode.com/problems/max-area-of-island/
"""
import unittest


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        g_len = len(grid)
        r_len = len(grid[0])
        cur = 0
        ans = 0

        def dfs(r: int, c: int) -> None:
            nonlocal cur
            if not 0 <= r < g_len or not 0 <= c < r_len or grid[r][c] != 1:
                return 0
            # mark cell as visited so that it's not counted again
            grid[r][c] = "v"
            cur += 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                cur = 0
                dfs(i, j)
                ans = max(ans, cur)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.maxAreaOfIsland(
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                ]
            ),
            6,
        )
        self.assertEqual(t.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]), 0)


if __name__ == "__main__":
    unittest.main()
