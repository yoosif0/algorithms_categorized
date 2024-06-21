"""
@nested-tags:matching/dict/trie/any_substring
https://leetcode.com/problems/string-matching-in-an-array
"""

import unittest
import pprint

pp = pprint.PrettyPrinter(indent=4)


VISITED = "VISITED"


class Solution:
    def stringMatching(self, a: list[str]) -> list[str]:
        m = {}

        def add(s: str):
            cur = m
            for i in range(len(s)):
                if s[i] not in cur:
                    cur[s[i]] = {}
                cur = cur[s[i]]
                if VISITED not in cur:
                    cur[VISITED] = 0
                cur[VISITED] += 1

        def times_visited(s: str) -> int:
            cur = m
            for i in range(len(s)):
                if s[i] not in cur:
                    return 0
                cur = cur[s[i]]
            return 0 if VISITED not in cur else cur[VISITED]

        for word in a:
            for i in range(len(word)):
                add(word[i : len(word)])

        ans = []
        for word in a:
            if times_visited(word) >= 2:
                ans.append(word)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.stringMatching(["mass", "as", "hero", "superhero"]), ["as", "hero"]
        )
        self.assertEqual(
            t.stringMatching(["mass", "as", "ma", "hero", "superhero"]),
            ["as", "ma", "hero"],
        )


if __name__ == "__main__":
    unittest.main()
