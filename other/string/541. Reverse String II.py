"""
https://leetcode.com/problems/reverse-string-ii/
"""
import unittest


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        should_reverse = True
        sentence = []
        word = []
        for i in range(len(s)):
            word.append(s[i])
            if len(word) == k or i == len(s) - 1:
                word = word[::-1] if should_reverse else word
                sentence.append("".join(word))
                should_reverse = not should_reverse
                word = []
        return "".join(sentence)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.reverseStr("onetwoten", 3), "enotwonet")
        self.assertEqual(t.reverseStr("abcdefg", 2), "bacdfeg")


if __name__ == "__main__":
    unittest.main()
