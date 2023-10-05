"""
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
#optimization
"""
import unittest


class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cur = 0
        ans = 0

        def dfs(r: int, c: int):
            nonlocal cur
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] <= 0:
                return
            cur += grid[r][c]
            grid[r][c] = -1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c > 0:
                    cur = 0
                    dfs(i, j)
                    ans = max(cur, ans)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]), 7
        )


if __name__ == "__main__":
    unittest.main()
