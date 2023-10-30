"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

import unittest


class Solution:
    def reverseWords(self, a: str) -> str:
        a = a[::-1].split()[::-1]
        return " ".join(a)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc"
        )


if __name__ == "__main__":
    unittest.main()
