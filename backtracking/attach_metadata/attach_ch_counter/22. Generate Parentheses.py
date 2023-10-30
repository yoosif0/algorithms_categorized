"""
https://leetcode.com/problems/generate-parentheses/
            (                                         
        ()        ((
    ()(        (((    (()
    ()()       ((()     (())                   
               ((())
               ((()))
#combination
attaching counter of characters to save time instead of counting characters in each function call
"""
from collections import Counter
import unittest


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def dfs(tmp: str, cnt):
            if cnt[0] == n and cnt[1] == n:
                ans.append(tmp)
            elif cnt[0] == cnt[1]:
                dfs(tmp + "(", (cnt[0] + 1, cnt[1]))
            elif cnt[0] == n:
                dfs(tmp + ")", (cnt[0], cnt[1] + 1))
            else:
                dfs(tmp + "(", (cnt[0] + 1, cnt[1]))
                dfs(tmp + ")", (cnt[0], cnt[1] + 1))

        dfs("", (0, 0))
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.generateParenthesis(1), ["()"])
        self.assertEqual(
            obj.generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )


if __name__ == "__main__":
    unittest.main()
