"""
https://leetcode.com/problems/pascals-triangle
        1
       1,1
      1,2,1
     1,3,3,1
    1,4,6,4,1
   1,5,10,10,5,1
  1,6,15,20,15,6,1
 1,7,21,35,35,21,7,1
#combination
"""

import unittest


class Solution:
    def generate(self, m: int) -> list[list[int]]:
        dp = [[None for _ in range(i + 1)] for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
            dp[i][i] = 1
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.generate(1), [[1]])
        self.assertEqual(
            t.generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        )


if __name__ == "__main__":
    unittest.main()
