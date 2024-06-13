"""
@nested-tags:binary_search/lhs_rhs
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

import unittest


class Solution:
    def searchRange(self, a: list[int], x: int) -> list[int]:
        if not len(a):
            return [-1, -1]
        l = 0
        r = len(a) - 1
        while l < r:
            mid = (l + r) // 2
            if a[mid] < x:
                l = mid + 1
            else:
                r = mid
        first = l
        l = first
        r = len(a) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if a[mid] > x:
                r = mid - 1
            else:
                l = mid
        last = r
        return [first, last] if a[first] == x else [-1, -1]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(t.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
        self.assertEqual(t.searchRange([], 0), [-1, -1])


if __name__ == "__main__":
    unittest.main()
