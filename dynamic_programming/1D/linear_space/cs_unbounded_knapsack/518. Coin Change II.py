"""
https://leetcode.com/problems/coin-change-ii
#count_combinations

Add the number of combinations of the previous coin
8 [2,5]
moving not in order (each coin)
0 1 2 3 4 5 6 7 8 9 10 11 12 13
1 0 1 0 1 1 1 1 1 1 2  1  2   1
"""

import unittest


class Solution:
    def change(self, t: int, cs: list[int]) -> int:
        if t == 0:
            return 1
        dp = [0 for _ in range(t + 1)]
        cs = list(filter(lambda x: x <= t, cs))
        for c in cs:
            dp[c] += 1
            for i in range(c + 1, len(dp)):
                dp[i] += dp[i - c]
        return dp[-1]


"""
2 5
1 2 3 4 5 6 7 8 9 10 11 12
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.change(5, [1, 2, 5]), 4)
        self.assertEqual(t.change(3, [2]), 0)
        self.assertEqual(t.change(10, [10]), 1)
        self.assertEqual(t.change(7, [2, 5]), 1)
        self.assertEqual(t.change(8, [2, 5]), 1)
        self.assertEqual(t.change(12, [2, 5]), 2)
        self.assertEqual(t.change(13, [2, 5]), 1)
        self.assertEqual(t.change(0, [7]), 1)


if __name__ == "__main__":
    unittest.main()
