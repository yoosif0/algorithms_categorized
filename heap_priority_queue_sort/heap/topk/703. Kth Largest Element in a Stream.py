"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
#min_heap
#keep_len_k

[1, 4, 5, 8, 2]
[1, 2, 4, 5, 8]
"""

import heapq
import unittest


class KthLargest:
    def __init__(self, k: int, a: list[int]):
        h = a[:k]
        heapq.heapify(h)
        for i in range(k, len(a)):
            heapq.heappushpop(h, a[i])
        self.h = h
        self.k = k

    def add(self, x: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, x)
        else:
            heapq.heappushpop(self.h, x)
        return self.h[0]


class Test(unittest.TestCase):
    def test(self):
        # obj = KthLargest(3, [1, 4, 5, 8, 2])
        obj = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(obj.add(3), 4)
        self.assertEqual(obj.add(5), 5)
        self.assertEqual(obj.add(10), 5)
        self.assertEqual(obj.add(9), 8)
        self.assertEqual(obj.add(4), 8)


if __name__ == "__main__":
    unittest.main()
