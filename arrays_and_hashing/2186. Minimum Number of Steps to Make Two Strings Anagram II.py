"""
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
"""


import unittest
import collections
import math


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        m = collections.Counter(s)
        m2 = collections.Counter(t)
        # count what's in s but not in t
        n = 0
        for k in m:
            if m[k] > m2[k]:
                n += m[k] - m2[k]
        # count what's in t but not in s
        n2 = 0
        for k in m2:
            if m2[k] > m[k]:
                n2 += m2[k] - m[k]
        return n + n2


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.minSteps("leetcode", "coats"), 7)


if __name__ == "__main__":
    unittest.main()
