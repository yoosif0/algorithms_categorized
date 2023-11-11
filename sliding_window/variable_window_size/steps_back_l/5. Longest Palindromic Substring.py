"""
https://leetcode.com/problems/longest-palindromic-substring/
b a 
"""
import unittest


class Solution:
    def longestPalindrome(self, s):
        # l of best palindrome and it's length
        l = 0
        w_len = 1

        def update(r, steps_back):
            nonlocal l
            nonlocal w_len
            l2 = r - w_len - steps_back
            if l2 < 0:
                return False
            sub = s[l2 : r + 1]
            if sub == sub[::-1]:
                l, w_len = l2, w_len + steps_back + 1
                return True

        for r in range(1, len(s)):
            # check 1 step before other than the new expanded r (expand l too and not only r)
            if update(r, 1):
                continue
            # check 0 steps before (expand r only)
            update(r, 0)
        return s[l : l + w_len]


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.longestPalindrome("babad"), "bab")
        self.assertEqual(t.longestPalindrome("cbbd"), "bb")
        self.assertEqual(t.longestPalindrome("cabbad"), "abba")
        self.assertEqual(t.longestPalindrome("ccc"), "ccc")


if __name__ == "__main__":
    unittest.main()
