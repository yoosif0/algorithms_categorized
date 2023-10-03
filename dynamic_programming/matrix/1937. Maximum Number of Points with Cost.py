"""
https://leetcode.com/problems/maximum-number-of-points-with-cost/


The idea here is to fill rows from bottom to up. For each cell we make sure it has the best
outcome by comparing it to all cells down
While filling the bottom row, I should gather info about which columns are promising
Currently getting TLE
#not_completely_solved
"""
import unittest


class Solution:
    def maxPoints(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[None for _ in range(n)] for _ in range(m)]
        # fill bottom row
        for j in range(n):
            dp[m - 1][j] = grid[m - 1][j]
        # fill rows from down to top
        for i in range(m - 2, -1, -1):
            down_row = dp[i + 1]
            for j in range(n):
                # compare with all numbers in the down row accounting for cost
                max_points = 0
                for k, val in enumerate(down_row):
                    cost = abs(k - j)
                    max_points = max(val - cost, max_points)
                dp[i][j] = max_points + grid[i][j]
        # get max value from top row
        ans = 0
        top_row = dp[0]
        for p in top_row:
            ans = max(p, ans)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]), 9)


if __name__ == "__main__":
    unittest.main()
