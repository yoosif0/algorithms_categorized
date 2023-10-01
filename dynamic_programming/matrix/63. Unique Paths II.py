"""
https://leetcode.com/problems/unique-paths-ii/

211
101
111

10
11
"""
import unittest


class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # if there is a block in the cell, then 0
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                # assign 1 to the target (it's not blocked)
                if i == m - 1 and j == n - 1:
                    dp[i][j] = 1
                    continue
                right = dp[i + 1][j] if i < m - 1 else 0
                down = dp[i][j + 1] if j < n - 1 else 0
                dp[i][j] = right + down
        return dp[0][0]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2
        )
        self.assertEqual(t.uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)
        self.assertEqual(t.uniquePathsWithObstacles([[0, 0], [0, 1]]), 0)


if __name__ == "__main__":
    unittest.main()
