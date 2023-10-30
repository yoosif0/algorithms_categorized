"""
https://leetcode.com/problems/longest-palindromic-substring/
b a 
"""
import unittest


class Solution:
    def longestPalindrome(self, s):
        # l of best palindrome and it's length
        ans_l = 0
        ans_len = 1

        def update(r, steps_back):
            nonlocal ans_l
            nonlocal ans_len
            l = r - ans_len - steps_back
            if l < 0:
                return False
            sub = s[l : r + 1]
            if sub == sub[::-1]:
                ans_l, ans_len = l, ans_len + steps_back + 1
                return True

        for r in range(1, len(s)):
            # check 1 step before other than the new expanded r (expand l too and not only r)
            if update(r, 1):
                continue
            # check 0 steps before (expand r only)
            update(r, 0)
        return s[ans_l : ans_l + ans_len]


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.longestPalindrome("babad"), "bab")
        self.assertEqual(t.longestPalindrome("cbbd"), "bb")
        self.assertEqual(t.longestPalindrome("cabbad"), "abba")
        self.assertEqual(t.longestPalindrome("ccc"), "ccc")


if __name__ == "__main__":
    unittest.main()
