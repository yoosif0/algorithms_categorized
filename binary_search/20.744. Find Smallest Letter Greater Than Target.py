"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target
"""

import unittest


class Solution:
    def nextGreatestLetter(self, a: list[int], t: int) -> int:
        if t >= a[-1]:
            return a[0]
        l = 0
        r = len(a) - 1
        while l < r:
            mid = (l + r) // 2
            if a[mid] <= t:
                l = mid + 1
            else:
                r = mid
        return a[l]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.nextGreatestLetter(["c", "f", "j"], "a"), "c")
        self.assertEqual(t.nextGreatestLetter(["c", "f", "j"], "c"), "f")
        self.assertEqual(t.nextGreatestLetter(["x", "x", "y", "y"], "z"), "x")
        self.assertEqual(t.nextGreatestLetter(["c", "f", "j"], "j"), "c")


if __name__ == "__main__":
    unittest.main()
