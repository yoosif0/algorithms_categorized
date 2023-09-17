"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

from bisect import bisect_left
import unittest


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        index = bisect_left(self.nums, val)
        self.nums.insert(index, val)
        return self.nums[-self.k]


class Test(unittest.TestCase):
    def test(self):
        obj = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(obj.add(3), 4)
        self.assertEqual(obj.add(5), 5)
        self.assertEqual(obj.add(10), 5)
        self.assertEqual(obj.add(9), 8)
        self.assertEqual(obj.add(4), 8)


if __name__ == "__main__":
    unittest.main()
