"""
@nested-tags:matching/kmp
"""

import unittest


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # kmp
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            v = dp[i - 1]
            while v and s[i] != s[v]:
                v = dp[v - 1]
            dp[i] = v + (s[i] == s[v])
        return dp[-1] and dp[-1] % (len(s) - dp[-1]) == 0


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.repeatedSubstringPattern("abab"), True)
        self.assertEqual(t.repeatedSubstringPattern("aba"), False)
        self.assertEqual(t.repeatedSubstringPattern("abcabcabcabc"), True)


if __name__ == "__main__":
    unittest.main()
