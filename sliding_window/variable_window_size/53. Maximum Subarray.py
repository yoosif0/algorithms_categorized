"""
https://leetcode.com/problems/maximum-subarray/description/

[-2, 1, -3, 4, -1, 2, 1, -5, 4]
-2: window value -2
1:  1 > wv, wv=1
-3: -3 is not > wv; wv-2 
4: 4>-2 wv=4
-1: wv=3
2: wv=5
1: wv=6
-5: wv=1
4: wv=5

also #greedy
"""


import unittest


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        window_val = nums[0]
        ans = window_val
        for r in range(1, len(nums)):
            num = nums[r]
            window_val = max(window_val + num, num)
            ans = max(window_val, ans)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == "__main__":
    unittest.main()
