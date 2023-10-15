"""
https://leetcode.com/problems/remove-outermost-parentheses/
(()())(())
(()


     ((((()()))))
ans:  (((

(()())(()) (()(()))
()()()()(())
"""

import unittest


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        ans = []
        for ch in s:
            if ch == "(":
                st.append(ch)
                if len(st) >= 2:
                    ans.append(ch)
            else:
                st.pop()
                if len(st) >= 1:
                    ans.append(ch)
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.removeOuterParentheses("(()())(())"), "()()()")
        self.assertEqual(
            obj.removeOuterParentheses("(()())(())(()(()))"), "()()()()(())"
        )


if __name__ == "__main__":
    unittest.main()
