"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""

from typing import Dict
import unittest


class Node:
    def __init__(self, char: str):
        self.char = char
        self.dict: Dict[str, Node] = {}
        self.completes_a_word = False


class WordDictionary:
    def __init__(self):
        self.tree = Node("")

    def addWord(self, word: str) -> None:
        pointer = self.tree
        for char in word:
            if char not in pointer.dict:
                pointer.dict[char] = Node(char)
            pointer = pointer.dict[char]
        pointer.completes_a_word = True

    def search_inner(self, word: str, pointer: Node) -> bool:
        pointer = self.tree if not pointer else pointer
        for i, char in enumerate(word):
            if char == ".":
                for char in pointer.dict:
                    suffix = word[i + 1 :]
                    res = self.search_inner(suffix, pointer.dict[char])
                    if res:
                        return True
                return False
            else:
                if char not in pointer.dict:
                    return False
                pointer = pointer.dict[char]
        return pointer.completes_a_word

    def search(self, word: str) -> bool:
        return self.search_inner(word, self.tree)


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
