"""
https://leetcode.com/problems/find-the-difference/
"""

import collections
import unittest


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m = collections.Counter(s)
        m2 = collections.Counter(t)
        for ch in m2:
            if m2[ch] > m[ch]:
                return ch


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.findTheDifference("abcd", "abcde"), "e")


if __name__ == "__main__":
    unittest.main()
