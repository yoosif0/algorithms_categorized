"""
https://leetcode.com/problems/product-of-array-except-self/

Each num in nums should have a before product and after product saved in an array or hash map and the result
is before * after
"""


import unittest


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # fill before product
        before_product = []
        cur = 1
        for num in nums:
            before_product.append(cur)
            cur *= num

        # fill after product
        after_product = [1 for _ in range(len(nums))]
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            after_product[i] = cur
            cur *= num

        # fill ans
        ans = []
        for i in range(len(nums)):
            ans.append(before_product[i] * after_product[i])
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])


if __name__ == "__main__":
    unittest.main()
