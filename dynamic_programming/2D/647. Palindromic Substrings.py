"""
https://leetcode.com/problems/palindromic-substrings/
#count_combinations
#palindrome
#O(n2/2)_time

  zczaaaz 
z 1
c 01
z  01
a   01
a   11
a    11
z     01

Logic: check whether each 2 consectutive chars are similar (palis).
Then check for 3 consecutive chars, then 4,5, till you check the whole s.
Whether 3,4,5,... consecutive substrings forms a pali is function of 
1) whether the the inner substring is a pali and 2) whether first and 
last chars are equal

Control: fill dp table diagonally starting by ones. Then fill the second
diagonal which is just below the first, then the third diagonal, etc till
you comeplete a triangle

This is like 5.Longest_Palindromic_Substrings.py

"""

import unittest

def f(s: str) -> str:
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    ans = len(s)
    # fill 1s diagonal across
    for i in range(len(s)):
        dp[i][i] = 1
    
    # fill 2nd diagonal representing 2 similar consec characters
    for i in range(len(s)-1):
        start = s[i]
        end   = s[i+1]
        if start == end:
            dp[i+1][i] = 1
            ans += 1

    # prnt2d(dp,s,s) 
    for d in range(2,len(s)):
        for i in range(len(s)-d):
            start = s[i]
            end   = s[i+d]
            # diagonal is whethere inner substring is palindrome
            diagonal = dp[i+d-1][i+1]
            if start == end and diagonal != 0:
                dp[i+d][i] = 1
                ans += 1
    return ans

class Solution:
    def countSubstrings(self, s: str) -> int:
        return f(s)

a = [
    ["abc", 3],
    ["aaa", 6],
    ["zaaaz", 9],
    ["zaz", 4],
    ["fdsklf", 6],
    ["zczaaaz", 12]
]
class Test(unittest.TestCase):
    def test(self):
        for x in a:
            self.assertEqual(f(x[0]), x[1])
        


if __name__ == "__main__":
    unittest.main()
