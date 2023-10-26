"""
https://leetcode.com/problems/k-closest-points-to-origin/
#max_heap
"""

import heapq
import unittest


class Solution:
    def kClosest(self, a: list[list[int]], k: int) -> list[list[int]]:
        h = [(-(a[i][0] * a[i][0] + a[i][1] * a[i][1]), a[i]) for i in range(k)]
        heapq.heapify(h)
        for i in range(k, len(a)):
            heapq.heappushpop(h, (-(a[i][0] * a[i][0] + a[i][1] * a[i][1]), a[i]))
        return [tp[1] for tp in h]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertEqual(obj.kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
        self.assertEqual(
            obj.kClosest([[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]], 1),
            [[1, 1]],
        )


if __name__ == "__main__":
    unittest.main()
