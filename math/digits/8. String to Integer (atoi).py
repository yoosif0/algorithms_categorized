"""
https://leetcode.com/problems/string-to-integer-atoi/
"""

import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)
        l = 0
        while l < len(s) and s[l] == " ":
            l += 1
        if l == len(s):
            return 0
        fl = False
        if s[l] == "-":
            fl = True
            l += 1
        elif s[l] == "+":
            l += 1
        ans = 0
        while l < len(s) and s[l].isnumeric():
            ans = ans * 10 + int(s[l])
            l += 1
        ans = -ans if fl else ans
        if ans > INT_MAX:
            return INT_MAX
        elif ans < INT_MIN:
            return INT_MIN
        else:
            return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.myAtoi("42"), 42)
        self.assertEqual(t.myAtoi("     -42"), -42)
        self.assertEqual(t.myAtoi("4193 with words"), 4193)
        self.assertEqual(t.myAtoi(""), 0)
        self.assertEqual(t.myAtoi("+1"), 1)


if __name__ == "__main__":
    unittest.main()
