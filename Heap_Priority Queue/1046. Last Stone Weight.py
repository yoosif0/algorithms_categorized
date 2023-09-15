"""
https://leetcode.com/problems/last-stone-weight/
"""

import unittest
from collections import deque
from bisect import bisect_left


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()
        q = deque(stones)
        while len(q) > 1:
            first = q.pop()
            second = q.pop()
            diff = first - second
            index = bisect_left(q, diff)
            q.insert(index, diff)
        return q[0]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)


if __name__ == "__main__":
    unittest.main()
