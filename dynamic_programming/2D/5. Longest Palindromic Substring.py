"""
https://leetcode.com/problems/longest-palindromic-substring/
#optimization
#palindrome
#O(n2/2)_time

  b a b a d           
b 1 
a 0 1 
b 3 0 1 
a 0 3 0 1
d 0 0 0 0 1

  c b b d
c 1
b 0 1
b 0 2 1
d 0 0 0 1

Logic: We fist check if 2 consective characters are the same.
If they are => we have a palindrome of 2. Then we check palis
with distance of 3,4,5,etc which is a function of 2 things.
1) the first and last character equal.
2) inner substring is a pali. 
By inner, I mean the substring excluding start and end. 

Control: We fill the dp table diagonally. From top left till
bottom right. Going in step by step. Each diagonal filling 
represents the distance between start and last character.
Each diagonal filling is shorter than the one before by 1.
Till we reach the last diagonal with a distance of 1. When we
check whether the whole string is a palindrome.

This is like 647.Palindromic_Substrings.py
"""

import unittest
from algoutils.twod_array import prnt2d

def solve(s: str) -> str:
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    # fill 1s diagonal across
    for i in range(len(s)):
        dp[i][i] = 1
    
    # fill 2nd diagonal representing 2 similar consec characters
    for i in range(len(s)-1):
        start = s[i]
        end   = s[i+1]
        if start == end:
            dp[i+1][i] = 2

    # prnt2d(dp,s,s) 
    for d in range(2,len(s)):
        for i in range(len(s)-d):
            start = s[i]
            end   = s[i+d]
            # diagonal is length of the inner palindrome (if exists)
            diagonal = dp[i+d-1][i+1]
            if start == end and diagonal != 0:
                dp[i+d][i] = 2 + diagonal

    # prnt2d(dp,s,s) 
    # find max value in dp (which is longest palindrome)
    # cur is (max_length, start_index, last_index)
    cur = (1,0,0)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if dp[j][i] > cur[0]:
                cur = (dp[j][i], i, j)
    ans = s[cur[1]:cur[2]+1]
    return ans

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return solve(s)

a = [
    ["babad", "bab"],
    ["cbbd", "bb"],
    ["bb", "bb"],
]

class Test(unittest.TestCase):
    def test(self):
        for x in a:
            self.assertEqual(solve(*x[:-1]),x[-1])
        


if __name__ == "__main__":
    unittest.main()
