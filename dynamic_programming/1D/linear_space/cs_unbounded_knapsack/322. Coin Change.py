"""
@nested-tags:knapsack/unbounded
https://leetcode.com/problems/coin-change/
#optimization
"""

import sys
import unittest


class Solution:
    def coinChange(self, cs: list[int], t: int) -> int:
        if t == 0:
            return 0
        dp = [-1 for _ in range(t + 1)]
        cs = list(filter(lambda x: x <= t, cs))
        for c in cs:
            dp[c] = 1
            for i in range(c + 1, len(dp)):
                if dp[i - c] == -1:
                    pass
                elif dp[i] == -1:
                    dp[i] = dp[i - c] + 1
                else:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[-1] == -1 else dp[-1]


"""
2 5
0 1 2 3 4 5 6 7 8 9 10 11 12
    1   2   3   4   5       
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.coinChange([2, 5], 12), 3)
        self.assertEqual(t.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(t.coinChange([2], 3), -1)
        self.assertEqual(t.coinChange([1], 0), 0)
        self.assertEqual(t.coinChange([456, 117, 5, 145], 1459), 23)
        self.assertEqual(t.coinChange([3, 7, 405, 436], 8839), 25)


if __name__ == "__main__":
    unittest.main()
