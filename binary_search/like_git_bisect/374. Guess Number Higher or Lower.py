"""
https://leetcode.com/problems/guess-number-higher-or-lower/
"""

import unittest

picked = None


def guess(n: int):
    if n == picked:
        return 0
    if n < picked:
        return 1
    return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            if guess(m) == 1:
                l = m + 1
            else:
                r = m
        return l


class Test(unittest.TestCase):
    def test(self):
        global picked
        t = Solution()
        picked = 6
        self.assertEqual(t.guessNumber(10), 6)
        picked = 1
        self.assertEqual(t.guessNumber(1), 1)
        picked = 1
        self.assertEqual(t.guessNumber(2), 1)


if __name__ == "__main__":
    unittest.main()
