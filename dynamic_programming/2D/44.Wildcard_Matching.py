"""
https://leetcode.com/problems/wildcard-matching
     x   ?   a  *  
x    1   0   0  0 
a    0   1   0  0  
a    0   0   1  1  
b    0   0   0  0
c    0   0
a    0

     x   a   *    
x    1   0   0   
a    0   1   1    
a    0   0   1    


"""

import unittest
from algoutils.twod_array import prnt2d

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # padding so that the dp loop works for "i-1" and "j-1"
        s = "x"+s
        p = "x"+p

        dp = [[0 for _ in range(len(p))] for _ in range(len(s))]
        # fill padding (first row and first column). 
        # First column is all 0 (except for first cell)
        dp[0][0]=1
        for k in range(1, len(dp[0])):
            asterisk = p[k] == "*"
            if asterisk and dp[0][k-1]:
                dp[0][k] = 1

        for i in range(1,len(s)):
            for j in range(1,len(p)):
                eq = p[j][0] == s[i] or p[j][0] == "?"
                asterisk = p[j] == "*"
                # any of those conditions means a current match
                if (    
                    (eq and dp[i-1][j-1])
                    or 
                    (asterisk and dp[i][j-1])
                    or 
                    (asterisk and dp[i-1][j])
                ):
                    dp[i][j] = 1
        # prnt2d(dp,s,p)
        return dp[-1][-1] == 1

a = [
    ["aa", "p", False],
    ["aa", "*", True],
    ["cb", "?a", False],
]

class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        for case in a:
            self.assertEqual(t.isMatch(case[0], case[1]), case[2])
        
            

if __name__ == "__main__":
    unittest.main()
