"""
https://leetcode.com/problems/valid-parenthesis-string/
(()))))***


"""
import unittest


class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt = 0
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "*":
                cnt += 1
            elif cnt:
                cnt -= 1
            else:
                return False
        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")" or s[i] == "*":
                cnt += 1
            elif cnt:
                cnt -= 1
            else:
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
        # self.assertEqual(
        #     obj.checkValidString("(((((()*)(*)*))())())(()())())))((**)))))(()())()"),
        #     False,
        # )


"""
0123456789012345678901234567890123456789012345678
(((((()*)(*)*))())())(()())())))((**)))))(()())()



"""

if __name__ == "__main__":
    unittest.main()
