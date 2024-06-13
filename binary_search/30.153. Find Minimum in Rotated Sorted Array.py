"""
@nested-tags:binary_search/remove_from_l,binary_search/rotated_sorted_arr
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

import unittest


class Solution:
    def findMin(self, a: list[int]) -> int:
        l = 0
        r = len(a) - 1
        while l < r:
            mid = (l + r) // 2
            if a[mid] > a[r]:
                l = mid + 1
            else:
                r = mid
        return a[l]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(t.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(t.findMin([11, 13, 15, 17]), 11)
        self.assertEqual(t.findMin([3, 1, 2]), 1)


if __name__ == "__main__":
    unittest.main()
