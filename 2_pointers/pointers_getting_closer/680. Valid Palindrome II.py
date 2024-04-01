"""
https://leetcode.com/problems/valid-palindrome-ii/

dabcad
"""

import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if it's odd then it should be a palindrome
        if len(s) % 2 != 0:
            return s[: len(s) // 2] == s[(len(s) // 2) + 1 :]
        else:
            if s[: len(s) // 2] == s[(len(s) // 2) :]:
                return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isPalindrome("aba"), True)
        # self.assertEqual(obj.isPalindrome("abca"), False)
        self.assertEqual(obj.isPalindrome("abc"), False)
        self.assertEqual(obj.isPalindrome("abba"), True)


if __name__ == "__main__":
    unittest.main()
