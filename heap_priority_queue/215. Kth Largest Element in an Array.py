"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import unittest
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(obj.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


if __name__ == "__main__":
    unittest.main()
