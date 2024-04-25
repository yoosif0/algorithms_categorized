"""
https://leetcode.com/problems/search-insert-position/
both bisect_left and bisect_right works because the arr has distinct values. If not, the question should tell use what to do if the insert value equals one of the values in the array. if we should put the new val to the left, we do bisect left 
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
