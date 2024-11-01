"""
https://leetcode.com/problems/regular-expression-matching

ab*c*d*bf* 
This pattern makes branchgin/dfs/exponential time crucial.
When you see "ab", should you count b as one of "b*"?
If you did, the "b" at the end of the pattern will not find a match.
And you will mistakenly return False.
If you ignored the first "b", what will you do with "abbf" and "abbbf"?
We should return true for all these strings. 
"""

import unittest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
convert to this format => [s*, a, ., b*, c, .*, d].
For easier parsing
        """
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
        solved = False

        
        memo = set() #memoize
        # i is s index. 
        # p is relevant part of pattern
        def dfs(i,p):
            key = str(i)+str(p)
            if key in memo:
                return
            else:
                memo.add(key)
            # dd = [i,p]
            tail_p = p[1:] if len(p)>1 else []
            if i == len(s) and len(p)==0:
                nonlocal solved 
                solved = True
                # dd.append("solved")
            elif len(p) == 0:
                # dd.append("p finished")
                pass
            # len of 2 => it's followed by "*"
            elif len(p[0]) == 2:
                # dd.append("has *")
                ch = p[0][0]
                # check for "*" => 0,l1 or more
                for j in range(len(s)-i+1):
                    new_p = j*[ch] + tail_p
                    # dd.append("new_p: "+ str(new_p))
                    dfs(i, new_p)
            elif i<len(s) and s[i] == p[0] or p[0] == ".":
                dfs(i+1, tail_p)
                # dd.append("match")
            # print(dd)

        dfs(0,a)
        return solved

a = [
    ["aaaaaaaaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*", False],
    ["a", "ab*", True],
    ["aaa", "a*a", True],
    ["ab", ".*c", False],
    ["aab", "c*a*b", True],
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
