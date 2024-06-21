"""
@nested-tags:matching/kmp
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

import unittest


class Solution:
    def strStr(self, s: str, s2: str) -> int:
        # kmp
        s = s2 + "_" + s
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            v = dp[i - 1]
            while v and s[i] != s[v]:
                v = dp[v - 1]
            dp[i] = v + (s[i] == s[v])
            if dp[i] == len(s2):
                return i - 2 * len(s2)
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.strStr("sadbutsad", "sad"), 0)
        self.assertEqual(t.strStr("leetcode", "leeto"), -1)
        self.assertEqual(t.strStr("mississippi", "issip"), 4)
        self.assertEqual(t.strStr("a", "a"), 0)
        self.assertEqual(t.strStr("aaa", "aa"), 0)


if __name__ == "__main__":
    unittest.main()
