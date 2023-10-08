"""
https://leetcode.com/problems/longest-palindromic-substring/
#optimization
#palindrome
#O(n2/2)_time
#improve_on_backtracking
"""

import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        ans = [0, 0]
        dp = [[None for _ in range(m)] for _ in range(m)]
        # d is the difference between l and r
        for d in range(1, len(s)):
            for l in range(m - d):
                r = l + d
                inner_is_ok = dp[l + 1][r - 1] if d > 2 else True
                dp[l][r] = s[l] == s[r] and inner_is_ok
                if dp[l][r] and (r - l + 1) > (ans[1] - ans[0] + 1):
                    ans = [l, r]
        return s[ans[0] : ans[1] + 1]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.longestPalindrome("babad"), "bab")
        self.assertEqual(obj.longestPalindrome("cbbd"), "bb")
        self.assertEqual(obj.longestPalindrome("bb"), "bb")


if __name__ == "__main__":
    unittest.main()
