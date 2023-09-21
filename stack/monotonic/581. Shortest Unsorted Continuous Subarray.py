"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray

[2,6,4,8,10,9,15]
First find the start index by having a monotonic increasing stack.
The reason we need another monotonic decreasing stack to find end index is that sometimes we have 
repeated numbers that need to be sorted like [1, 3, 2, 2, 2]


"""
import unittest


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        # find start index
        start = len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                start = min(start, stack.pop())
            stack.append(i)

        # find end index
        end = -1
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                end = max(end, stack.pop())
            stack.append(i)

        return 0 if end == -1 else end - start + 1


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]), 5)
        self.assertEqual(obj.findUnsortedSubarray([1, 2, 3, 4]), 0)
        self.assertEqual(obj.findUnsortedSubarray([1]), 0)
        self.assertEqual(obj.findUnsortedSubarray([5, 4, 3, 2, 1]), 5)
        self.assertEqual(obj.findUnsortedSubarray([1, 3, 2, 2, 2]), 4)
        self.assertEqual(obj.findUnsortedSubarray([2, 3, 3, 2, 4]), 3)
        self.assertEqual(obj.findUnsortedSubarray([1, 2, 4, 5, 3]), 3)
        self.assertEqual(obj.findUnsortedSubarray([1, 3, 5, 2, 4]), 4)
        self.assertEqual(obj.findUnsortedSubarray([1, 3, 5, 4, 2]), 4)


if __name__ == "__main__":
    unittest.main()
