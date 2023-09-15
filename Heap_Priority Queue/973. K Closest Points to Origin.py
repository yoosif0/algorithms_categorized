"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""

import math
import unittest
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = []
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            tup = (point, distance)
            distances.append(tup)
        distances.sort(key=lambda x: x[1])
        closest_tuples = distances[0:k]
        ans = []
        for tup in closest_tuples:
            ans.append(tup[0])
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertEqual(obj.kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])


if __name__ == "__main__":
    unittest.main()
