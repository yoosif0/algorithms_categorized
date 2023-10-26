"""
https://leetcode.com/problems/search-insert-position/
"""


import bisect
import unittest


class Solution:
    def searchInsert(self, a: list[int], t: int) -> int:
        return bisect.bisect_left(a, t)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(t.searchInsert([1, 3, 5, 6], 7), 4)


if __name__ == "__main__":
    unittest.main()
