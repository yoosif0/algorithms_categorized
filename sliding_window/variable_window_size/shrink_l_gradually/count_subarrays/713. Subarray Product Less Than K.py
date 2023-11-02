"""
https://leetcode.com/problems/subarray-product-less-than-k/
The trick here is how you add to cnt "r - l + 1". We can confidently add more to cnt because we know all numbers are positive and since the whole subbaray product is below k so each subarray of the subarray is also below k. 
note we can't solve this problem with sliding window if negative numbers are included because the condition won't be monotonic.

[10,5,2,6]
10: w=10 [10]
5:  w=50 [5], [10,5]
2:  w=10 [2], [5,2]
6:  w=60 [6], [5,2,6], [2,6]
"""
import unittest


class Solution:
    def numSubarrayProductLessThanK(self, a: list[int], k: int) -> int:
        l = 0
        w = 1
        cnt = 0
        for r in range(len(a)):
            # expand from r and then compress from l if needed
            w *= a[r]
            while l <= r and w >= k:
                w /= a[l]
                l += 1
            cnt += r - l + 1
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numSubarrayProductLessThanK([10, 5, 2, 6], 100), 8)
        self.assertEqual(t.numSubarrayProductLessThanK([1, 1, 1], 1), 0)
        self.assertEqual(t.numSubarrayProductLessThanK([1, 2, 3], 0), 0)


if __name__ == "__main__":
    unittest.main()
