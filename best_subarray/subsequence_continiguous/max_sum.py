import unittest

"""
[5, -7, 1, 4, 3, 2, 9, -2, 3]
5 best
-7: temp best is -2, keep 5 as best
1:  temp best is 1 since 1 is greater than 1+ -2, keep 5 as best
4:  add to the one before so temp best is 5, keep 5 as best
3:  add to the one before so temp best is 8, best is now 8 
2:  best and temp best are 10
9:  best and temp best are 19
-2: temp best is 17. best is 19
3:  temp best is 20. best is 20

"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_end_here = max_so_far = nums[0]
        for _, num in enumerate(nums[1:]):
            max_end_here = max(max_end_here + num, num)
            max_so_far = max(max_end_here, max_so_far)
        return max_so_far


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxSubArray([5, -7, 1, 4, 3, 2, 9, -2, 3]), 20)
        self.assertEqual(t.maxSubArray([-2, 3, 2, -1, 10]), 14)
        self.assertEqual(t.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == "__main__":
    unittest.main()
