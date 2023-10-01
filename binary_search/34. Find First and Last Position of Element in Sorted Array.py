"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
import bisect
import unittest


class Solution:
    def searchRange(self, a: list[int], target: int) -> list[int]:
        l = bisect.bisect_left(a, target)
        if l >= len(a) or a[l] != target:
            return [-1, -1]
        r = bisect.bisect_right(a, target)
        return [l, r - 1]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(t.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
        self.assertEqual(t.searchRange([], 0), [-1, -1])


if __name__ == "__main__":
    unittest.main()
