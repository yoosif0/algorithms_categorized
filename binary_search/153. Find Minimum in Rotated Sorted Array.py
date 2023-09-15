"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

import unittest


class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(t.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(t.findMin([11, 13, 15, 17]), 11)
        self.assertEqual(t.findMin([3, 1, 2]), 1)


if __name__ == "__main__":
    unittest.main()
