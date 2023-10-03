"""
https://leetcode.com/problems/maximum-subarray/

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
"""


import unittest


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        w = nums[0]
        ans = w
        for r in range(1, len(nums)):
            num = nums[r]
            w = max(w + num, num)
            ans = max(w, ans)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == "__main__":
    unittest.main()
