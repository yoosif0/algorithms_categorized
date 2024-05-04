"""
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

5 [250, 5900]
250 1475 x 4             1475
"""

import math
import unittest


class Solution:
    def minimizedMaximum(self, n: int, a: list[int]) -> int:
        avg = (sum(a) - 1) // n + 1
        if avg > min(a):
            return max(a)
        return avg


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minimizedMaximum(6, [11, 6]), 3)
        self.assertEqual(t.minimizedMaximum(2, [5, 7]), 7)
        self.assertEqual(t.minimizedMaximum(7, [15, 10, 10]), 5)
        self.assertEqual(t.minimizedMaximum(1, [10000]), 10000)
        # self.assertEqual(t.minimizedMaximum(5, [250, 5900]), 1475)
        # self.assertEqual(t.minimizedMaximum(22, [25,11,29,6,24,4,29,18,6,13,25,30]), 13)
        self.assertEqual(t.minimizedMaximum(3, [2, 10, 6]), 10)


if __name__ == "__main__":
    unittest.main()
