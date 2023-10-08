"""
https://leetcode.com/problems/longest-palindromic-substring/
  a a t e q k l q a a q t b t a e
a   1
a
t
e
q
k
l
q
a                   1 
a                    
q
t
b
t
a
e


 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 
a 1
a  2
a   3
a    4
a     5
a      6
a
a
a
a
a
a
a
a
a
a
a
a
a
a
go back till you find a true
"""
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        for i in range(len(s) - 1, -1, 0):
            if s[i] == s[i + 1]:
                length = 2
                l = i - 1
                r = i + 2
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        length += 2
                ans = max(ans, length)

        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = int(i & 1) + dp[i // 2]
        return dp[n]


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.countBits(1), [0, 1])
        self.assertEqual(t.countBits(2), [0, 1, 1])
        self.assertEqual(t.countBits(3), [0, 1, 1, 2])
        self.assertEqual(t.countBits(4), [0, 1, 1, 2, 1])
        self.assertEqual(t.countBits(5), [0, 1, 1, 2, 1, 2])


if __name__ == "__main__":
    unittest.main()
