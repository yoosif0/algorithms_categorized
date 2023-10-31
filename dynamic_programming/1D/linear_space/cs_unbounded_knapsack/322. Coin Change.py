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

"""
0 1 2 3 4 5 6 7 8 9 10 11
0 
"""


class Solution:
    def coinChange(self, cs: list[int], n: int) -> int:
        dp = [n + 1 for _ in range(n + 1)]
        dp[0] = 0
        for c in cs:
            for i in range(c, len(dp)):
                dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[n] > n else dp[n]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(t.coinChange([2], 3), -1)
        self.assertEqual(t.coinChange([1], 0), 0)
        self.assertEqual(t.coinChange([456, 117, 5, 145], 1459), 23)


if __name__ == "__main__":
    unittest.main()
