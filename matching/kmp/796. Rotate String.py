"""
@nested-tags:matching/kmp/append_s_again
This shouldn't be solved with kmp because the string is very small
https://leetcode.com/problems/rotate-string
"""

import unittest


class Solution:
    def rotateString(self, s: str, pat: str) -> bool:
        if len(pat) != len(s):
            return False
        # kmp
        # append s again because it might need to be rotated
        s = pat + "_" + s + s
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            v = dp[i - 1]
            while v and s[i] != s[v]:
                v = dp[v - 1]
            dp[i] = v + (s[i] == s[v])
            if dp[i] == len(pat):
                return True
        return False


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.rotateString("abcde", "cdeab"), True)


if __name__ == "__main__":
    unittest.main()
