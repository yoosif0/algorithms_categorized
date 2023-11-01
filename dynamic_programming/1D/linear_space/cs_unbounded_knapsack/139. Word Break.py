"""
https://leetcode.com/problems/word-break/
#decision
"""
from collections import Counter
import functools
import unittest


class Solution:
    def wordBreak(self, s: str, cs: list[str]) -> bool:
        found = False

        @functools.cache
        def rcrs(s: str):
            nonlocal found
            if s == "":
                found = True
                return
            for c in cs:
                if c == s[: len(c)]:
                    rcrs(s[len(c) :])

        rcrs(s)
        return found


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.wordBreak("leetcode", ["leet", "code"]), True)


if __name__ == "__main__":
    unittest.main()
