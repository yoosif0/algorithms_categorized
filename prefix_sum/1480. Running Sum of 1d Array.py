"""
https://leetcode.com/problems/running-sum-of-1d-array/
"""
from itertools import accumulate
import unittest


class Solution:
    def runningSum(self, a: list[int]) -> list[int]:
        return list(accumulate(a))


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])


if __name__ == "__main__":
    unittest.main()
