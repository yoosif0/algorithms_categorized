"""
https://leetcode.com/problems/minimum-size-subarray-sum/

[2,3,1,2,4,3]
[2,5,6,8,12,15]
2: ps=8  complement: 1 or less, l stay the same as 0
4: ps=12 complement: 5 or less, l go to 2
3: ps=15 complement: 8 or less, l go to 4
"""


import unittest
import sys
from bisect import bisect_right


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]):
        ans = sys.maxsize
        l = 0
        prefix_sums = []
        prefix_sum = 0
        for r in range(len(nums)):
            prefix_sum += nums[r]
            prefix_sums.append(prefix_sum)
            if prefix_sum < target:
                continue
            if prefix_sum > target:
                # find best l to reduce window as much as possible
                l = bisect_right(prefix_sums, prefix_sum - target)
            window_size = r - l + 1
            ans = min(window_size, ans)
        return 0 if ans == sys.maxsize else ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)
        self.assertEqual(t.minSubArrayLen(4, [1, 4, 4]), 1)
        self.assertEqual(t.minSubArrayLen(14, [1, 1, 1, 1, 1, 1, 1, 1]), 0)
        self.assertEqual(t.minSubArrayLen(9, [2, 3, 1, 2, 4, 2, 6, 3]), 2)
        self.assertEqual(t.minSubArrayLen(15, [1, 2, 3, 4, 5]), 5)


if __name__ == "__main__":
    unittest.main()
