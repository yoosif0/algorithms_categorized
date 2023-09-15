"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""
from typing import Dict
import unittest


class Node:
    def __init__(self, char: str):
        self.char = char
        self.dict: Dict[str, Node] = {}
        self.completes_a_word = False


class Trie:
    def __init__(self):
        self.tree = Node("")

    def insert(self, word: str) -> None:
        pointer = self.tree
        for char in word:
            if char not in pointer.dict:
                pointer.dict[char] = Node(char)
            pointer = pointer.dict[char]
        pointer.completes_a_word = True

    def search(self, word: str) -> bool:
        pointer = self.tree
        for char in word:
            if char not in pointer.dict:
                return False
            pointer = pointer.dict[char]
        return pointer.completes_a_word

    def startsWith(self, prefix: str) -> bool:
        pointer = self.tree
        for char in prefix:
            if char not in pointer.dict:
                return False
            pointer = pointer.dict[char]
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
