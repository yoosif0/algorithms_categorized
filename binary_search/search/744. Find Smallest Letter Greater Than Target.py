"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target
bisect_right because we're looking for something strictly greater than target.It means that equal vals are with smaller vals on left. Greater vals are on right
"""

import bisect
import unittest


class Solution:
    def nextGreatestLetter(self, a: list[int], t: int) -> int:
        i = bisect.bisect_right(a, t)
        return a[0] if i == len(a) else a[i]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.nextGreatestLetter(["c", "f", "j"], "a"), "c")
        self.assertEqual(t.nextGreatestLetter(["c", "f", "j"], "c"), "f")
        self.assertEqual(t.nextGreatestLetter(["x", "x", "y", "y"], "z"), "x")


if __name__ == "__main__":
    unittest.main()
