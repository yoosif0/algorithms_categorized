"""
@nested-tags:linked/trie,string_prefix_search,memoize,string_suffix_search
https://leetcode.com/problems/prefix-and-suffix-search
"""

import pprint

pp = pprint.PrettyPrinter(indent=4)

import unittest

WORD_INDEX = "word_index"


def buildTrie(a: list[int]):
    m = {}
    for i in range(len(a)):
        cur = m
        for ch in a[i]:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
            if WORD_INDEX not in cur:
                cur[WORD_INDEX] = []
            cur[WORD_INDEX].append(i)
    return m


def getWordIndecis(m: dict, s: str) -> list[int]:
    cur = m
    for ch in s:
        if ch not in cur:
            return []
        cur = cur[ch]
    return cur[WORD_INDEX]


class WordFilter:
    def __init__(self, a: list[int]):
        self.m = buildTrie(a)
        self.memo = {}
        a = [x[::-1] for x in a]
        self.m2 = buildTrie(a)
        del a

    def f(self, pref: str, suff: str) -> int:
        key_name = pref + "," + suff
        if key_name in self.memo:
            return self.memo[key_name]
        st = getWordIndecis(self.m, pref)
        st2 = getWordIndecis(self.m2, suff[::-1])
        p = len(st) - 1
        p2 = len(st2) - 1
        while p >= 0 and p2 >= 0:
            if st[p] > st2[p2]:
                p -= 1
            elif st[p] < st2[p2]:
                p2 -= 1
            else:
                self.memo[key_name] = st[p]
                return self.memo[key_name]
        self.memo[key_name] = -1
        return self.memo[key_name]


class Test(unittest.TestCase):
    def test(self):
        obj = WordFilter(
            [
                "apple",
                "ant",
                "ann",
                "arm",
                "beetle",
                "barbel",
                "barbie",
                "baby",
                "cat",
                "car",
            ]
        )
        self.assertEqual(obj.f("a", "t"), 1)
        self.assertEqual(obj.f("a", "nt"), 1)
        self.assertEqual(obj.f("b", "nt"), -1)
        self.assertEqual(obj.f("a", "le"), 0)
        self.assertEqual(obj.f("be", "le"), 4)


if __name__ == "__main__":
    unittest.main()
