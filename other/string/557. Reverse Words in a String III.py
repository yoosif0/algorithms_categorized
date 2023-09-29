"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = []
        word = []
        for char in s:
            if char == " ":
                if len(word):
                    sentence.append("".join(word[::-1]))
                    word = []
                continue
            word.append(char)
        if len(word):
            sentence.append("".join(word[::-1]))
        return " ".join(sentence)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc"
        )


if __name__ == "__main__":
    unittest.main()
