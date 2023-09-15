"""
https://leetcode.com/problems/unique-paths/
"""
import unittest
import functools


# @functools.lru_cache(maxsize=None)
# def uniquePaths(self, m: int, n: int) -> int:
#     if m == 1 or n == 1:
#         return 1
#     return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [
            [1 if (j == n - 1 or i == m - 1) else 0 for j in range(n)] for i in range(m)
        ]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        # for l in dp:
        #     print("\t".join(map(str, l)))
        return dp[0][0]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.uniquePaths(3, 7), 28)
        self.assertEqual(t.uniquePaths(4, 7), 84)
        # self.assertEqual(t.uniquePaths(3, 7), 28)
        # self.assertEqual(t.uniquePaths(4, 7), 84)
        # self.assertEqual(t.uniquePaths(3, 2), 3)


if __name__ == "__main__":
    unittest.main()
