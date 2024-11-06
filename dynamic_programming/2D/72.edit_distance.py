"""
https://leetcode.com/problems/min-distance/description/

#bottom_up

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
# from algoutils.twod_array import prnt2d
from algoutils.list_node import ListNode

class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]
#     def minDistance(self, s: str, s2: str) -> str:
#         s  +=  "!"
#         s2 +=  "!"
#         dp = [[0 for _ in range(len(s))] for _ in range(len(s2))]
#         # fill padding
#         for i in range(len(s)):
#             dp[-1][i] = len(s) - i - 1
#         for i in range(len(s2)):
#             dp[i][-1] = len(s2) - i - 1
#         """
# For each subproblem, you either 
# 1) do no operation : when the first char matches:
# 2) add char        
# 3) remove char
# 4) substitute char
#         """
#         for i in range(len(s2)-2, -1, -1):
#             for j in range(len(s)-2, -1,  -1):
#                 diagonal = dp[i+1][j+1]
#                 if s2[i] == s[j]:
#                     dp[i][j] = diagonal # no operation
#                 else:
#                     # pick best among add, remove, or substitute
#                     right    = dp[i][j+1]
#                     bottom   = dp[i+1][j]
#                     dp[i][j] = 1 + min(right, bottom, diagonal)
#         # prnt2d(dp,s2,s,2)
#         return dp[0][0]
#

class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.minDistance("horse", "ros"), 3)
        self.assertEqual(obj.minDistance("deassert", "assorting"), 6)
        self.assertEqual(obj.minDistance("zoologicoarchaeologist", "zoogeologist"), 10)

"""
zoologicoarchaeologist
zoologicoarchaeologist
zoogeologist

"""

if __name__ == "__main__":
    unittest.main()
