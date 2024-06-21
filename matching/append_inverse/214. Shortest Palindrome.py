"""
@nested-tags:matching/kmp,matching/append_inverse,hard
https://leetcode.com/problems/shortest-palindrome

find the longest palindrome substring starts from index 0
best explanation: https://leetcode.com/problems/shortest-palindrome/solutions/60113/clean-kmp-solution-with-super-detailed-explanation/
"""

import unittest


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # kmp
        inv = s[::-1]
        sk = s + "_" + inv
        dp = [0 for _ in range(len(sk))]
        j = 0
        i = 1
        while i < len(sk):
            if sk[i] == sk[j]:
                dp[i] = j + 1
                i += 1
                j += 1
            elif j != 0:
                j = dp[j - 1]
            else:
                dp[i] = 0
                i += 1
        # dp[-1] is the length of palindrome found. We need to add the rest of inv.
        # Note that if dp[-1]==0, it means we should add the whole inv string (which is the worst case)
        return inv[: len(inv) - dp[-1]] + s


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.shortestPalindrome("abcd"), "dcbabcd")
        self.assertEqual(t.shortestPalindrome("aacecaaa"), "aaacecaaa")


if __name__ == "__main__":
    unittest.main()
