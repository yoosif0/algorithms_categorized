"""
https://leetcode.com/problems/valid-palindrome/description/
"""
import unittest
import re


# def clean(s: str):
#     return re.sub("[^0-9a-zA-Z]+", "", s).lower()


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # def isPalindrome(self, s: str) -> bool:
    #     s = clean(s)
    #     return s == s[::-1]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isPalindrome("A man, a plan, a canal: Panama"), True)


if __name__ == "__main__":
    unittest.main()
