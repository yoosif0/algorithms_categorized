"""
@nested-tags:matching/kmp/append_s_again
https://leetcode.com/problems/repeated-string-match
"""

import unittest


class Solution:
    def repeatedStringMatch(self, a: str, pat: str) -> int:
        ans = 1
        # keep appending till you at least reach the length of pat
        b = a
        while len(b) < len(pat):
            b += a
            ans += 1

        # you might need to append again one time for something like b=abcd and pat=cdab
        for j in range(2):
            b = j * a + b
            # kmp
            s = pat + "_" + b
            dp = [0 for _ in range(len(s))]
            for i in range(1, len(s)):
                v = dp[i - 1]
                while v and s[i] != s[v]:
                    v = dp[v - 1]
                dp[i] = v + (s[i] == s[v])
                if dp[i] == len(pat):
                    return ans + j
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.repeatedStringMatch("abcd", "cdabcdab"), 3)
        self.assertEqual(t.repeatedStringMatch("a", "aa"), 2)
        self.assertEqual(t.repeatedStringMatch("abc", "cabcabca"), 4)


if __name__ == "__main__":
    unittest.main()
