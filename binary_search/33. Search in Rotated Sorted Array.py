"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Search for the pivot (minIndex which I already solved before). See if the target is to the right or left of the 
pivot by comparing the target to the right most value. If it's larger than it so the target is on the 
left portion. If not then it's in the right portion. Then we do a binary search on the correct portion.
Remember to add the missed indecis to the result if you searched the right portion.
"""

import unittest


class Solution:
    def findMinIndex(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def find(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return -1

    def search(self, nums: list[int], target: int) -> int:
        min_i = self.findMinIndex(nums)
        if target <= nums[-1]:
            res = self.find(nums[min_i:], target)
            if res == -1:
                return res
            return res + min_i
        return self.find(nums[0:min_i], target)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.search([4, 5, 6, 7, 0, 1, 2], 4), 0)
        self.assertEqual(t.search([1], 1), 0)
        self.assertEqual(t.search([1, 3], 3), 1)
        self.assertEqual(t.search([3, 1], 3), 0)


if __name__ == "__main__":
    unittest.main()
