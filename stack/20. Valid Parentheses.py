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
        map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            # if it's an opening char, append to stack
            if char in map:
                stack.append(char)
                continue
            if len(stack) == 0:
                return False
            # check if the closing char match what it should close
            last_open_char = stack[-1]
            if char == map[last_open_char]:
                stack.pop()
            else:
                return False
        return len(stack) == 0


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
