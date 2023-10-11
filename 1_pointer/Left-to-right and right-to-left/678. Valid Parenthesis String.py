"""
https://leetcode.com/problems/valid-parenthesis-string/
(()))))***


"""
import unittest


class Solution:
    def checkValidString(self, s: str) -> bool:
        open = 0
        close = 0
        for ch in s:
            if ch == "(" or ch == "*":
                open += 1
            else:
                close += 1
            if close > open:
                return False
        open = 0
        close = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == "(":
                open += 1
            else:
                close += 1
            if open > close:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.checkValidString("("), False)
        self.assertEqual(obj.checkValidString("()"), True)
        self.assertEqual(obj.checkValidString("(*)"), True)
        self.assertEqual(obj.checkValidString("(*))"), True)
        self.assertEqual(obj.checkValidString("((((*))"), False)
        self.assertEqual(obj.checkValidString("(()))))"), False)
        self.assertEqual(obj.checkValidString("(()))))***"), False)
        self.assertEqual(obj.checkValidString("*)()"), True)
        self.assertEqual(
            obj.checkValidString("(((((()*)(*)*))())())(()())())))((**)))))(()())()"),
            False,
        )


"""
0123456789012345678901234567890123456789012345678
(((((()*)(*)*))())())(()())())))((**)))))(()())()



"""

if __name__ == "__main__":
    unittest.main()
