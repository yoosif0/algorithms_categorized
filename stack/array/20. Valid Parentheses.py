"""
https://leetcode.com/problems/valid-parentheses/
{[()()[]]}
{[(
{[
{[(
{[
{[[
{[
{

If it's an opening char, append to stack. If it's a closing char, it should complement the last element in stack

"""

import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        m = {"(": ")", "{": "}", "[": "]"}
        st = []
        for ch in s:
            # if it's an opening char, append to stack
            if ch in m:
                st.append(ch)
            # check if the closing char match what it should close
            elif st and ch == m[st[-1]]:
                st.pop()
            else:
                return False
        return len(st) == 0


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isValid("()[]{}"), True)
        self.assertEqual(obj.isValid("()"), True)
        self.assertEqual(obj.isValid("(]"), False)
        self.assertEqual(obj.isValid("{[()()[]]}"), True)
        self.assertEqual(obj.isValid("{"), False)


if __name__ == "__main__":
    unittest.main()
