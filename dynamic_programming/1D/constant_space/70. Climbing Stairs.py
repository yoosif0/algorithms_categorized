"""
https://leetcode.com/problems/climbing-stairs/
4

2 2
2 1 1
1 2 1
1 1 2
1 1 1 1

#optimization
"""


import unittest


# O(n) space
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0 for _ in range(n + 1)]
#         dp[0] = 1
#         dp[1] = 1
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 2] + dp[i - 1]
#         return dp[n]


# O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        cur = 1
        for _ in range(2, n + 1):
            cur, prev = cur + prev, cur
        return cur


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.climbStairs(2), 2)
        self.assertEqual(t.climbStairs(3), 3)
        self.assertEqual(t.climbStairs(4), 5)


if __name__ == "__main__":
    unittest.main()
