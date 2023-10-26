"""
https://leetcode.com/problems/last-stone-weight/
"""

import heapq
import unittest


class Solution:
    def lastStoneWeight(self, a: list[int]) -> int:
        h = [-num for num in a]
        heapq.heapify(h)
        while len(h) > 1:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)


if __name__ == "__main__":
    unittest.main()
