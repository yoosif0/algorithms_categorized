"""
https://leetcode.com/problems/coin-change-ii
#combination
#need_to_revise

0 1 2 3 4 5 6
1 1 2 2 3 4 5

3:1 1 1 or 1 2 
4: 1111 or 22 or 2 11
5: 11111 or 221 or 2111 or   5
6: 111111 or 222 or 21111 or 51 or  2211
"""
import unittest


class Solution:
    def change(self, n: int, cs: list[int]) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for c in cs:
            for i in range(c, len(dp)):
                dp[i] += dp[i - c]
        return dp[n]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.change(5, [1, 2, 5]), 4)
        self.assertEqual(t.change(3, [2]), 0)
        self.assertEqual(t.change(10, [10]), 1)


if __name__ == "__main__":
    unittest.main()
