"""
https://leetcode.com/problems/minimum-operations-to-halve-array-sum
The trick here is to know that reducing the biggest numbers is the way to reduce the total to half in the least amount of steps
"""

import heapq
import unittest


class Solution:
    def halveArray(self, h: list[int]) -> int:
        h = [-i for i in h]
        heapq.heapify(h)
        ans = 0
        cur = sum(h) / 2
        while h and cur < 0:
            x = heapq.heappop(h) / 2
            cur -= x
            ans += 1
            heapq.heappush(h, x)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.halveArray([5, 19, 8, 1]), 3)


if __name__ == "__main__":
    unittest.main()
