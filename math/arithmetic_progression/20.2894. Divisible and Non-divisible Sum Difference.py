"""
https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
"""

import unittest


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        all = n * (n + 1) // 2
        divisible = m * (n // m) * (n // m + 1) // 2
        return all - 2 * divisible


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.differenceOfSums(10, 3), 19)
        self.assertEqual(t.differenceOfSums(80, 7), 2316)


if __name__ == "__main__":
    unittest.main()
