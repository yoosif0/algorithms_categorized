"""
https://leetcode.com/problems/two-sum/
"""
import unittest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numberToIndexStore = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numberToIndexStore and numberToIndexStore[complement] != i:
                return [numberToIndexStore[complement], i]
            numberToIndexStore[num] = i
        return []


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(t.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(t.twoSum([3, 2, 4, 9, 4], 8), [2, 4])


if __name__ == "__main__":
    unittest.main()
