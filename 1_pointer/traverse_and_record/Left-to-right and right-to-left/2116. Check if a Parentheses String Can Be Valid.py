"""
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
(()(() 000100
use lock

(()))) 000100
use lock. add to bdgt


"""
import unittest


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open = 0
        close = 0
        for i, ch in enumerate(s):
            if ch == "(" or locked[i] == "0":
                open += 1
            else:
                close += 1
            if close > open:
                return False
        if (open + close) % 2 != 0:
            return False
        open = 0
        close = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == ")" or locked[i] == "0":
                close += 1
            else:
                open += 1
            if open > close:
                return False
        if (open + close) % 2 != 0:
            return False
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        # self.assertEqual(obj.canBeValid("))()))", "010100"), True)
        # self.assertEqual(obj.canBeValid("()()", "0000"), True)
        # self.assertEqual(obj.canBeValid(")", "0"), False)
        self.assertEqual(obj.canBeValid(")(", "00"), True)


if __name__ == "__main__":
    unittest.main()
