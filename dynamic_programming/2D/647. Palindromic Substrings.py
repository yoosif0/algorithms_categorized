"""
https://leetcode.com/problems/palindromic-substrings/
#count_combinations
#palindrome
#O(n2/2)_time
#improve_on_backtracking

0123456
zczaaaz 
dp[0][1]=False
dp[1][2]=False
dp[2][3]=False
dp[3][4]=True
dp[4][5]=True
dp[5][6]=False
---
dp[0][2]= s[0]==s[2] = True
dp[1][3]= s[1]==s[3] = False
dp[2][4]= s[2]==s[4] = False
dp[3][5]= True
dp[4][6]= False
---
dp[0][3]= dp[1][2] and s[0]==s[3] = False
dp[1][4]= False
dp[2][5]= False
dp[3][6]= False
---
dp[0][4]= dp[1][3] and s[0]==s[4] = False 
dp[1][5]= False
dp[2][6]= True
----
dp[0][5]= dp[1][4] and s[0]==s[5] = False 
dp[1][6]= False 
-----
dp[0][6]= dp[1][5] and s[0]==s[6] = False 
"""

import unittest


class Solution:
    def countSubstrings(self, s: str) -> int:
        m = len(s)
        ans = m
        dp = [[None for _ in range(m)] for _ in range(m)]
        # d is the difference between l and r
        for d in range(1, len(s)):
            for l in range(m - d):
                r = l + d
                # if the diff is 2 or less, this comparison doesn't make sense
                inner_is_ok = dp[l + 1][r - 1] if d > 2 else True
                dp[l][r] = s[l] == s[r] and inner_is_ok
                if dp[l][r]:
                    ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.countSubstrings("abc"), 3)
        self.assertEqual(obj.countSubstrings("aaa"), 6)
        self.assertEqual(obj.countSubstrings("zaaaz"), 9)
        self.assertEqual(obj.countSubstrings("zaz"), 4)
        self.assertEqual(obj.countSubstrings("fdsklf"), 6)
        self.assertEqual(obj.countSubstrings("zczaaaz"), 12)


if __name__ == "__main__":
    unittest.main()
