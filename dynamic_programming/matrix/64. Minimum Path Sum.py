"""
https://leetcode.com/problems/minimum-path-sum/

--4
--4
--5

"""
import unittest


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[None for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = dp[i + 1][n - 1] + grid[i][n - 1]
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = dp[m - 1][j + 1] + grid[m - 1][j]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                down = dp[i + 1][j]
                right = dp[i][j + 1]
                dp[i][j] = min(down, right) + grid[i][j]
        return dp[0][0]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
        self.assertEqual(t.minPathSum([[1, 2, 3], [4, 5, 6]]), 12)
        self.assertEqual(
            t.minPathSum(
                [
                    [9, 9, 0, 8, 9, 0, 5, 7, 2, 2, 7, 0, 8, 0, 2, 4, 8],
                    [4, 4, 2, 7, 6, 0, 9, 7, 3, 2, 5, 4, 6, 5, 4, 8, 7],
                    [4, 9, 7, 0, 7, 9, 2, 4, 0, 2, 4, 4, 6, 2, 8, 0, 7],
                    [7, 7, 9, 6, 6, 4, 8, 4, 8, 7, 9, 4, 7, 6, 9, 6, 5],
                    [1, 3, 7, 5, 7, 9, 7, 3, 3, 3, 8, 3, 6, 5, 0, 3, 6],
                    [7, 1, 0, 7, 5, 0, 6, 6, 5, 3, 2, 6, 0, 0, 9, 5, 7],
                    [6, 5, 6, 3, 8, 1, 8, 6, 4, 4, 3, 4, 9, 9, 3, 3, 1],
                    [1, 0, 2, 9, 7, 9, 3, 1, 7, 5, 1, 8, 2, 8, 4, 7, 6],
                    [9, 6, 7, 7, 4, 1, 4, 0, 6, 5, 1, 9, 0, 3, 2, 1, 7],
                    [2, 0, 8, 7, 1, 7, 4, 3, 5, 6, 1, 9, 4, 0, 0, 2, 7],
                    [9, 8, 1, 3, 8, 7, 1, 2, 8, 3, 7, 3, 4, 6, 7, 6, 6],
                    [4, 8, 3, 8, 1, 0, 4, 4, 1, 0, 4, 1, 4, 4, 0, 3, 5],
                    [6, 3, 4, 7, 5, 4, 2, 2, 7, 9, 8, 4, 5, 6, 0, 3, 9],
                    [0, 4, 9, 7, 1, 0, 7, 7, 3, 2, 1, 4, 7, 6, 0, 0, 0],
                ]
            ),
            77,
        )


if __name__ == "__main__":
    unittest.main()
