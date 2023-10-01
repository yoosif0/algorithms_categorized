"""
https://leetcode.com/problems/unique-paths/
"""
import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # assign 1 to the column in most right and row most bottom
                if i == m - 1 or j == n - 1:
                    dp[i][j] = 1
                    continue
                right = dp[i + 1][j]
                down = dp[i][j + 1]
                dp[i][j] = right + down
        return dp[0][0]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.uniquePaths(3, 7), 28)
        self.assertEqual(t.uniquePaths(4, 7), 84)


if __name__ == "__main__":
    unittest.main()
