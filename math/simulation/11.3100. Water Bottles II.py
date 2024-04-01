"""
https://leetcode.com/problems/reverse-integer
"""

import unittest


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
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
                numExchange += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxBottlesDrunk(13, 6), 15)
        self.assertEqual(t.maxBottlesDrunk(10, 3), 13)


if __name__ == "__main__":
    unittest.main()
