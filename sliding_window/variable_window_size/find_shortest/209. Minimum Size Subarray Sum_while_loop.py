"""
https://leetcode.com/problems/minimum-size-subarray-sum/

[2,3,1,2,4,3]
Window 2
2 3  s5
231 s6
2312 s8 yes a4 s6 l1
3124 s7 yes a4 s7 


[1,1,1,1,4,3]
[1,2,3,4,8,11]
"""


import unittest
import sys


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]):
        ans = sys.maxsize
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                m = r - l + 1
                ans = min(m, ans)
                # try to shift l to the right as much as possible
                proposed_l, proposed_sum = l + 1, cur_sum - nums[l]
                if proposed_sum < target:
                    break
                cur_sum, l = proposed_sum, proposed_l
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
