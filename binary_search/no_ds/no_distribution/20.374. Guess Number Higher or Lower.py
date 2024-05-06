"""
https://leetcode.com/problems/guess-number-higher-or-lower/
"""

import unittest

picked = None


def guess(n: int):
    if n < picked:
        return 1
    elif n > picked:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = (l + r) // 2
            ans = guess(m)
            if ans == 1:
                l = m + 1
            elif ans == -1:
                r = m - 1
            else:
                return m


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
