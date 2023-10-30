"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""
from typing import Dict
import unittest


class Node:
    def __init__(self, ch: str):
        self.ch = ch
        self.m = {}
        self.fl = False


class Trie:
    def __init__(self):
        self.t = Node("")

    def insert(self, s: str) -> None:
        cur = self.t
        for ch in s:
            if ch not in cur.m:
                cur.m[ch] = Node(ch)
            cur = cur.m[ch]
        cur.fl = True

    def search(self, s: str) -> bool:
        cur = self.t
        for ch in s:
            if ch not in cur.m:
                return False
            cur = cur.m[ch]
        return cur.fl

    def startsWith(self, s: str) -> bool:
        cur = self.t
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
