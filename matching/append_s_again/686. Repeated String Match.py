"""
@nested-tags:matching/append_s_again,matching/kmp
https://leetcode.com/problems/repeated-string-match
"""

import unittest


class Solution:
    def repeatedStringMatch(self, s: str, pat: str) -> int:
        ans = 1
        # keep appending till you at least reach the length of pat
        ss = s
        while len(ss) < len(pat):
            ss += s
            ans += 1

        old_s = s
        # you might need to append again one time for something like ss=abcd and pat=cdab
        for k in range(2):
            ss = k * old_s + ss
            # kmp
            s = pat + "_" + ss
            dp = [0 for _ in range(len(s))]
            i = 1
            j = 0
            while i < len(s):
                if s[j] == s[i]:
                    dp[i] = j + 1
                    if dp[i] == len(pat):
                        return ans + k
                    i += 1
                    j += 1
                elif j != 0:
                    j = dp[j - 1]
                else:
                    dp[i] = 0
                    i += 1
        return -1


"""
000012340  12345678
cdabcdab_abcdabcdabcd
       j          i 
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.repeatedStringMatch("abcd", "cdabcdab"), 3)
        self.assertEqual(t.repeatedStringMatch("a", "aa"), 2)
        self.assertEqual(t.repeatedStringMatch("abc", "cabcabca"), 4)
        self.assertEqual(t.repeatedStringMatch("abc", "wxyz"), -1)


if __name__ == "__main__":
    unittest.main()
