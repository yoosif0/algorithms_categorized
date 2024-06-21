"""
@nested-tags:matching/dict/trie
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""

import unittest

IS_WORD = "!!"


class WordDictionary:
    def __init__(self):
        self.m = {}

    def addWord(self, s: str) -> None:
        cur = self.m
        for ch in s:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur[IS_WORD] = True

    def rr(self, s: str, cur) -> bool:
        for i, ch in enumerate(s):
            if ch == ".":
                for ch in cur:
                    if self.rr(s[i + 1 :], cur[ch]):
                        return True
                return False
            if ch not in cur:
                return False
            cur = cur[ch]
        return IS_WORD in cur

    def search(self, s: str, cur=None) -> bool:
        if not cur:
            cur = self.m
        for i in range(len(s)):
            ch = s[i]
            if ch == ".":
                for ch in cur:
                    if ch == IS_WORD:
                        continue
                    elif self.search(s[i + 1 :], cur[ch]):
                        return True
                return False
            elif ch not in cur:
                return False
            else:
                cur = cur[ch]
        return IS_WORD in cur


class Test(unittest.TestCase):
    def test(self):
        obj = WordDictionary()
        obj.addWord("car")
        obj.addWord("a")
        obj.addWord("a")
        obj.addWord("barber")
        self.assertEqual(obj.search("car"), True)
        self.assertEqual(obj.search("ca"), False)
        self.assertEqual(obj.search(".ar"), True)
        self.assertEqual(obj.search("b.r"), False)
        self.assertEqual(obj.search("ca."), True)
        self.assertEqual(obj.search("c."), False)
        self.assertEqual(obj.search("c.."), True)
        self.assertEqual(obj.search(".a."), True)
        self.assertEqual(obj.search("b.arb"), False)
        self.assertEqual(obj.search("a"), True)
        self.assertEqual(obj.search("aa"), False)
        self.assertEqual(obj.search("a."), False)


if __name__ == "__main__":
    unittest.main()
