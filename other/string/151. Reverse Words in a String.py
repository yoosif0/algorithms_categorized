"""
https://leetcode.com/problems/reverse-words-in-a-string/
"""
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = s.split(" ")
        arr_trim = []
        for word in sentence:
            if word == "":
                continue
            arr_trim.append(word)
        l = 0
        r = len(arr_trim) - 1
        while l < r:
            arr_trim[l], arr_trim[r] = arr_trim[r], arr_trim[l]
            l += 1
            r -= 1
        return " ".join(arr_trim)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(t.reverseWords("the sky is blue"), "blue is sky the")
        # self.assertEqual(t.reverseWords("   hello world   "), "world hello")
        # self.assertEqual(t.reverseWords(" a  good      example   "), "example good a")


if __name__ == "__main__":
    unittest.main()
