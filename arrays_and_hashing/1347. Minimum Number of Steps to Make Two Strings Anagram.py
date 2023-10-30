"""
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram
bab aba
b 1 not in t
a 1 not in s


leetcode practice
lodee 5 not in t
prai  4 not in s
ans = max(x,y)
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
        return max(n, n2)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.minSteps("bab", "aba"), 1)
        self.assertEqual(obj.minSteps("leetcode", "practice"), 5)


if __name__ == "__main__":
    unittest.main()
