"""
https://leetcode.com/problems/find-the-pivot-integer/
"""
import unittest


class Solution:
    def pivotInteger(self, n: int) -> int:
        a = [i for i in range(n + 1)]
        dp = [0 for _ in range(n + 1)]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + a[i]
        for i in range(1, len(dp)):
            if dp[-1] - dp[i] == dp[i - 1]:
                return i
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.pivotInteger(8), 6)
        self.assertEqual(t.pivotInteger(1), 1)
        self.assertEqual(t.pivotInteger(4), -1)


if __name__ == "__main__":
    unittest.main()
