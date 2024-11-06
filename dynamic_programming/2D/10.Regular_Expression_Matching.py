"""
https://leetcode.com/problems/regular-expression-matching
#improve_on_backtracking

     c*  a*  b

a    n   y   n 
a    n   y   n
b    n   n



     c   a*  r
c    y   y   n 
a    n   y   n
a    n   y   n
a    n   y   n
a    n   y   n
a    n   y   n
a    n   y   n
a    n   y   n
a    n   y   n
a    n   y   n
a    n   y   n
r    n   n   y

     "   c   a*  b*  r
"    y   n   
c        y   y   y   n 
a        n   y   y   n   
a        n   y   y   n 
a        n   y   y   n 
a        n   y   y   n 
r        n      



"""

import unittest
from algoutils.twod_array import prnt2d

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # padding so that the dp loop works for "i-1" and "j-1"
        s = "x"+s
        p = "x"+p

        # reformat p for easier parsing. 
        # New format looks like: ["x", "a*", "c", ".*"]
        a = []
        i = 0
        while True:
            if i == len(p):
                break
            elif i+1 < len(p) and p[i+1] == "*":
                a.append(p[i] + "*")
                i += 2
            else:
                a.append(p[i])
                i += 1
        p = a

        dp = [[0 for _ in range(len(p))] for _ in range(len(s))]
        # fill padding (first row and first column). 
        # First column is all 0 (except for first cell)
        dp[0][0]=1
        for k in range(1, len(dp[0])):
            asterisk = len(p[k]) == 2
            if asterisk and dp[0][k-1]:
                dp[0][k] = 1

        for i in range(1,len(s)):
            for j in range(1,len(p)):
                eq = p[j][0] == s[i] or p[j][0] == "."
                asterisk = len(p[j]) == 2
                # any of those conditions means a current match
                conds = [
                    eq and dp[i-1][j-1],
                    asterisk and dp[i][j-1], 
                    eq and asterisk and dp[i-1][j], 
                ]
                for k in range(len(conds)):
                    if conds[k]:
                        dp[i][j] = 1
        # prnt2d(dp,s,p)
        return dp[-1][-1] == 1

a = [
    ["aab", "c*a*b", True],
    ["a", "ab*", True],
    ["aaaaaaaaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*", False],
    ["aaa", "a*a", True],
    ["ab", ".*c", False],
    ["abcd", "d*", False],
    ["carrr", "c.trrr", False],
    ["car", "c.*t", False],
    ["aab", "c*a*b", True],
    ["caaaaar", "ca*r", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["cat", "c.t", True],
]

class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        for case in a:
            self.assertEqual(t.isMatch(case[0], case[1]), case[2])
        
            

if __name__ == "__main__":
    unittest.main()
