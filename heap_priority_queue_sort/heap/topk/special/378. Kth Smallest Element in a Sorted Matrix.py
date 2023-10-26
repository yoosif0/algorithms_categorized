"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
#max_heap
#matrix
"""

import heapq
import unittest


class Solution:
    def kthSmallest(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        h = []
        for i in range(m):
            for j in range(n):
                if len(h) < k:
                    h.append(-grid[i][j])
                    if len(h) == k:
                        heapq.heapify(h)
                else:
                    heapq.heappushpop(h, -grid[i][j])
        return -h[0]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13
        )


if __name__ == "__main__":
    unittest.main()
