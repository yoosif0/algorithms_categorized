"""
https://leetcode.com/problems/min-distance/description/

  horse!
r 332333
o 322222
s 432111
! 543210

= (1 or 0) + min(right, top, diagonal) 

# delete "h"          add char           substitute
solve(orse,ros)     solve(horse,os)     solve(orse,os)
"""

import unittest
from algoutils.twod_array import prnt2d

class Solution:
    def minDistance(self, s, s2):
        s  = "!" + s
        s2 = "!" + s2 
        dp = [[0] * (len(s2)) for _ in range(len(s))]

        # fill padding
        for i in range(len(s)):
            dp[i][0] = i
        for j in range(len(s2)):
            dp[0][j] = j

        """
For each subproblem, you either 
1) do no operation : when the first char matches:
2) add char        
3) remove char
4) substitute char
        """
        for i in range(1, len(s)):
            for j in range(1,len(s2)):
                diagonal = dp[i - 1][j - 1] 
                if s[i] == s2[j]: # do no operation
                    dp[i][j] = diagonal
                else:
                    # pick best among add, remove, or substitute
                    left     = dp[i][j-1] 
                    top      = dp[i-1][j] 
                    dp[i][j] = 1 + min(left, top, diagonal)
#        prnt2d(dp,s,s2,2)
        return dp[-1][-1]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.minDistance("horse", "ros"), 3)
        self.assertEqual(obj.minDistance("deassert", "assorting"), 6)
        self.assertEqual(obj.minDistance("zoologicoarchaeologist", "zoogeologist"), 10)

if __name__ == "__main__":
    unittest.main()
