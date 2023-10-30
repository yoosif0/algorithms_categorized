"""
https://leetcode.com/problems/coin-change/
#decision

1 2 5
1 2 3 4 5 6 7 8 9 10
1 1     1 2 2 3 3  2

2
1 2 3
n 1 


2 5
1 2 3 4 5 6 7
n 1 n 2 1 3 
"""
import unittest
import sys


class Solution:
    def coinChange(self, a: list[int], n: int) -> int:
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 0
        # remove coins bigger than n
        a = list(filter(lambda x: x <= n, a))
        for i in range(1, n + 1):
            aa = []
            for j in a:
                if i - j < 0 or dp[i - j] == -1:
                    continue
                aa.append(dp[i - j])
            if not aa:
                continue
            dp[i] = min(aa) + 1
        return dp[n]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(t.coinChange([2], 3), -1)
        self.assertEqual(t.coinChange([1], 0), 0)
        self.assertEqual(t.coinChange([456, 117, 5, 145], 1459), 23)


if __name__ == "__main__":
    unittest.main()
