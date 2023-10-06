"""
https://leetcode.com/problems/maximum-subarray/
[-2,1,-3,4,-1,2,1,-5,4]
if num >w:
    reduce w
#pos_neg

"""


import sys
import unittest


class Solution:
    def maxSubArray(self, a: list[int]) -> int:
        ans = -sys.maxsize
        w = 0
        l = 0
        for r in range(len(a)):
            w += a[r]
            while w < a[r]:
                w -= a[l]
                l += 1
            ans = max(w, ans)
        return ans


# # dp
# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         w = nums[0]
#         ans = w
#         for r in range(1, len(nums)):
#             num = nums[r]
#             w = max(w + num, num)
#             ans = max(w, ans)
#         return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == "__main__":
    unittest.main()
