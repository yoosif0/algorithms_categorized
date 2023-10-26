"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
#min_heap
#keep_len_k
"""

import unittest
import heapq


class Solution:
    def findKthLargest(self, a: list[int], k: int) -> int:
        h = a[:k]
        heapq.heapify(h)
        for i in range(k, len(a)):
            heapq.heappushpop(h, a[i])
        return h[0]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(obj.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


if __name__ == "__main__":
    unittest.main()
