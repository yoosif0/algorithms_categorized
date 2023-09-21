"""
https://leetcode.com/problems/climbing-stairs/
4

2 2
2 1 1
1 2 1
1 1 2
1 1 1 1
"""


import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 2] + dp[i - 1])
        return dp[n]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.climbStairs(2), 2)
        self.assertEqual(t.climbStairs(3), 3)
        self.assertEqual(t.climbStairs(4), 5)


if __name__ == "__main__":
    unittest.main()