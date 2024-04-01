"""
https://leetcode.com/problems/water-bottles-ii/
"""

import unittest


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        ans = 0
        empty = 0
        while full:
            ans += full
            empty += full
            full = 0
            while empty >= numExchange:
                full += 1
                empty -= numExchange
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numWaterBottles(9, 3), 13)
        self.assertEqual(t.numWaterBottles(15, 4), 19)


if __name__ == "__main__":
    unittest.main()
