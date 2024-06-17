"""
@nested-tags:prefix_sum/subarray
https://leetcode.com/problems/find-the-middle-index-in-array/
"""

from itertools import accumulate
import unittest


class Solution:
    def findMiddleIndex(self, a: list[int]) -> int:
        a = list(accumulate(a))
        for i in range(1, len(a)):
            if a[i - 1] == a[-1] - a[i]:
                return i
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findMiddleIndex([2, 3, -1, 8, 4]), 3)


if __name__ == "__main__":
    unittest.main()
