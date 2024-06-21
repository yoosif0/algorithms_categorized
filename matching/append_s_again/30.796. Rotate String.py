"""
@nested-tags:matching/append_s_again,matching/brute_force
https://leetcode.com/problems/rotate-string

The trick here is to know that appending s to itself should contain a substring of a rotation of s
brute force because s is very small
"""

import unittest


class Solution:
    def rotateString(self, s: str, pat: str) -> bool:
        if len(s) != len(pat):
            return False
        return pat in s + s


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.rotateString("abcde", "cdeab"), True)


if __name__ == "__main__":
    unittest.main()
