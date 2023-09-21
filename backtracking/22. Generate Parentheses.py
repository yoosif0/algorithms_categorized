"""
https://leetcode.com/problems/generate-parentheses/description/
            (                                         
        ()        ((
    ()(        (((    (()
    ()()       ((()     (())                   
               ((())
               ((()))
"""
import unittest


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans: list[str] = []

        def dfs(opened: int, closed: int, cur: str):
            if opened == n and closed == n:
                ans.append(cur)
                return

            def open():
                dfs(opened + 1, closed, cur + "(")

            def close():
                dfs(opened, closed + 1, cur + ")")

            if opened == closed:
                open()
                return
            if opened == n:
                close()
                return
            open()
            close()

        dfs(0, 0, "")
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
