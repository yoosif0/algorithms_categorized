"""
https://leetcode.com/problems/regular-expression-matching
#improve_on_backtracking


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

def f(s,p):
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
            if (
                (eq and dp[i-1][j-1]) or
                (asterisk and dp[i][j-1]) or
                (eq and asterisk and dp[i-1][j]) 
                ):
                dp[i][j] = 1
    # prnt2d(dp,s,p)
    print(dp)
    return dp[-1][-1] == 1


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return f(s,p)

a = [
    ["aab", "c*a*b", True],
    ["a", "ab*", True],
    # ["aaaaaaaaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*", False],
    # ["aaa", "a*a", True],
    # ["ab", ".*c", False],
    # ["abcd", "d*", False],
    # ["carrr", "c.trrr", False],
    # ["car", "c.*t", False],
    # ["aab", "c*a*b", True],
    # ["caaaaar", "ca*r", True],
    # ["aa", "a", False],
    # ["aa", "a*", True],
    # ["ab", ".*", True],
    # ["cat", "c.t", True],
]

class Test(unittest.TestCase):
    def test(self):
        for x in a:
            self.assertEqual(f(x[0], x[1]), x[2])
        
            

if __name__ == "__main__":
    unittest.main()
