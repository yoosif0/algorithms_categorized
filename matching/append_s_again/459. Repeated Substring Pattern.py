"""
https://leetcode.com/problems/repeated-substring-pattern
@nested-tags:matching/brute_force,matching/append_s_again

brute force works here becuase the string is small
"""

import unittest


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = s + s
        ss_minus = ss[1 : len(ss) - 1]
        return s in ss_minus


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.repeatedSubstringPattern("abab"), True)
        self.assertEqual(t.repeatedSubstringPattern("aba"), False)
        self.assertEqual(t.repeatedSubstringPattern("abcabcabcabc"), True)
        self.assertEqual(t.repeatedSubstringPattern("abaababaab"), True)
        self.assertEqual(t.repeatedSubstringPattern("a"), False)


if __name__ == "__main__":
    unittest.main()
