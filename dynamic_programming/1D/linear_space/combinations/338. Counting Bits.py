"""
#combinations
"""
from itertools import accumulate
import unittest


class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = int(i & 1) + dp[i // 2]
        return dp


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.countBits(1), [0, 1])
        self.assertEqual(t.countBits(2), [0, 1, 1])
        self.assertEqual(t.countBits(3), [0, 1, 1, 2])
        self.assertEqual(t.countBits(4), [0, 1, 1, 2, 1])
        self.assertEqual(t.countBits(5), [0, 1, 1, 2, 1, 2])


if __name__ == "__main__":
    unittest.main()
