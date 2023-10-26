"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
#min_heap
#keep_len_k
"""

import heapq
import unittest


class Solution:
    def maxProduct(self, a: list[int]) -> int:
        h = a[:2]
        heapq.heapify(h)
        for i in range(2, len(a)):
            heapq.heappushpop(h, a[i])
        return (h[0] - 1) * (h[1] - 1)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.maxProduct([3, 4, 5, 2]), 12)


if __name__ == "__main__":
    unittest.main()
