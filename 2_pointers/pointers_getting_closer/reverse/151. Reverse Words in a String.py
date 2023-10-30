"""
https://leetcode.com/problems/reverse-words-in-a-string/
"""
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()[::-1]
        return " ".join(s)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(t.reverseWords("   hello world   "), "world hello")
        self.assertEqual(t.reverseWords(" a  good      example   "), "example good a")


if __name__ == "__main__":
    unittest.main()
