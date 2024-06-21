"""
@nested-tags:matching/brute_force,not_solved
https://leetcode.com/problems/longest-happy-prefix
"""

import unittest


class Solution:
    def longestPrefix(self, s: str) -> str:
        i = 1
        while True:
            suf = word[i * k :]
            pre = word[: len(suf)]
            if suf == pre:
                return i
            i += 1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.longestPrefix("level"), "l")


if __name__ == "__main__":
    unittest.main()
