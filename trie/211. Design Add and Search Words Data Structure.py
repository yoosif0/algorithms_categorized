"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""

from collections import defaultdict
import unittest


class Node:
    def __init__(self):
        self.m = defaultdict(Node)
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.m = Node()

    def addWord(self, s: str) -> None:
        cur = self.m
        for ch in s:
            cur = cur.m[ch]
        cur.is_word = True

    def rr(self, s: str, cur: Node) -> bool:
        for i, ch in enumerate(s):
            if ch == ".":
                for ch in cur.m:
                    if self.rr(s[i + 1 :], cur.m[ch]):
                        return True
                return False
            if ch not in cur.m:
                return False
            cur = cur.m[ch]
        return cur.is_word

    def search(self, s: str) -> bool:
        return self.rr(s, self.m)


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
