"""
https://leetcode.com/problems/third-maximum-number/
"""

import sys
import unittest


class Solution:
    def thirdMax(self, a: list[int]) -> int:
        first_max = -sys.maxsize
        for i in a:
            first_max = max(first_max, i)
        second_max = -sys.maxsize
        for i in a:
            if i == first_max:
                continue
            second_max = max(second_max, i)
        third_max = -sys.maxsize
        for i in a:
            if i == first_max or i == second_max:
                continue
            third_max = max(third_max, i)
        return third_max if third_max != -sys.maxsize else first_max


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.thirdMax([3, 2, 1]), 1)
        self.assertEqual(obj.thirdMax([1, 2]), 2)


if __name__ == "__main__":
    unittest.main()
