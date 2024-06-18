"""
@nested-tags:linked/trie,string/search/prefix
https://leetcode.com/problems/implement-trie-prefix-tree/

{
 c: {a: {r: {is_word: True}}}

}
"""

import unittest

IS_WORD = "!!"


class Trie:
    def __init__(self):
        self.m = {}

    def insert(self, s: str) -> None:
        cur = self.m
        for ch in s:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur[IS_WORD] = True

    def search(self, s: str) -> bool:
        cur = self.m
        for ch in s:
            if ch not in cur:
                return False
            cur = cur[ch]
        return IS_WORD in cur

    def startsWith(self, s: str) -> bool:
        cur = self.m
        for ch in s:
            if ch not in cur:
                return False
            cur = cur[ch]
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
