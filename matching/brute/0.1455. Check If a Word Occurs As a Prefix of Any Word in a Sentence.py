"""
@nested-tags:matching/brute_force
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence

It's ok to brute force here since the input is tiny
"""

import unittest


class Solution:
    def isPrefixOfWord(self, sentence: str, pre: str) -> int:
        a = sentence.split(" ")
        for i in range(len(a)):
            if len(pre) > len(a[i]):
                continue
            if a[i][: len(pre)] == pre:
                return i + 1
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.isPrefixOfWord("i love eating burger", "burg"), 4)


if __name__ == "__main__":
    unittest.main()
