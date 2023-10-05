"""
https://leetcode.com/problems/house-robber-ii/
[30,1,5,22,60]
30:incl:30 excl:0
1: incl:1  excl:30
5: incl:35 excl:1   
22:incl:23 excl:35   


1: incl:1  excl:0
5: incl:5  excl:1   
22:incl:23 excl:5   
60:incl:65 excl:23   incl = num + prev_excl; excl = max(prev_incl, prev_excl)


This is similar to max sum non adjacent but the difference is that the array represents a circle.
This means that the first and last elements are adjacent. That's why I solved once while excluding the first element
and another while excluding the last element. I returned back the max
#optimization
"""

import unittest


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))

    def rob1(self, nums: list[int]) -> int:
        incl, excl = 0, 0
        for _, num in enumerate(nums):
            incl, excl = num + excl, max(incl, excl)
        return max(excl, incl)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.rob([30, 1, 5, 22, 60]), 65)


if __name__ == "__main__":
    unittest.main()
