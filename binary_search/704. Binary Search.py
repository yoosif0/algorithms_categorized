"""
https://leetcode.com/problems/binary-search/
Think about 
[-1,0,3,5,9,12] t=9
l=0;r=6; m=3; mv=5; 
l=4;r=6; m=5; mv=9;

[-1,0,3,5,9,12], t= 2
l=0;r=6;m=3;
l=0;r=3;m=1;
l=2;r=3;m=2;
l=2;r=2;m=2;


[2,5], t=5
l=0;r=2;m=1

[1] t=1
l=0 r=1 m=0
"""

import unittest
import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return -1

    # def search(self, nums: list[int], target: int) -> int:
    #     index = bisect.bisect_left(nums, target)
    #     if nums[index] == target:
    #         return index
    #     return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(t.search([-1, 0, 3, 5, 9, 12], 2), -1)
        self.assertEqual(t.search([2, 5], 5), 1)


if __name__ == "__main__":
    unittest.main()
