"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""
from collections import defaultdict
import unittest


class Node:
    def __init__(self):
        self.m = defaultdict(Node)
        self.is_word = False


class Trie:
    def __init__(self):
        self.m = Node()

    def insert(self, s: str) -> None:
        cur = self.m
        for ch in s:
            cur = cur.m[ch]
        cur.is_word = True

    def search(self, s: str) -> bool:
        cur = self.m
        for ch in s:
            if ch not in cur.m:
                return False
            cur = cur.m[ch]
        return cur.is_word

    def startsWith(self, s: str) -> bool:
        cur = self.m
        for ch in s:
            if ch not in cur.m:
                return False
            cur = cur.m[ch]
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Trie()
        obj.insert("car")
        self.assertEqual(obj.search("car"), True)
        self.assertEqual(obj.search("ca"), False)
        self.assertEqual(obj.startsWith("ca"), True)
        self.assertEqual(obj.startsWith("ba"), False)


if __name__ == "__main__":
    unittest.main()
