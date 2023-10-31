"""
https://www.youtube.com/watch?v=oBt53YbR9Kk at 3:52:42
0 1 2 3 4 5 6 7 8
t 
"""
import unittest


class Solution:
    def canSum(self, t: int, cs: list[int]) -> bool:
        dp = [False for _ in range(t + 1)]
        dp[0] = True
        for c in cs:
            for i in range(len(dp)):
                if dp[i] and i + c < len(dp):
                    dp[i + c] = True
        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.canSum(7, [2, 3]), True)
        self.assertEqual(t.canSum(7, [5, 3, 4, 7]), True)
        self.assertEqual(t.canSum(7, [2, 4]), False)
        self.assertEqual(t.canSum(8, [2, 3, 5]), True)
        self.assertEqual(t.canSum(300, [7, 14]), False)


if __name__ == "__main__":
    unittest.main()
