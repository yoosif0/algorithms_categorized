"""
@nested-tags:prefix_sum/subarray
https://leetcode.com/problems/find-pivot-index/

[1,7,3, 6, 5, 6]
0  1  2 3  4  5
[1,8,11,17,22,28]

[4,-3,5,-7,8]
0  1  2  3  4
[4,1, 6, -1,7]

"""

from itertools import accumulate
import unittest


class Solution:
    def pivotIndex(self, a: list[int]) -> int:
        a = list(accumulate(a, initial=0))
        for i in range(1, len(a)):
            if a[i - 1] == a[-1] - a[i]:
                return i - 1
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(t.pivotIndex([1, 2, 3]), -1)
        self.assertEqual(t.pivotIndex([4, -3, 5, -7, 8]), 2)
        self.assertEqual(t.pivotIndex([2, 1, -1]), 0)


if __name__ == "__main__":
    unittest.main()
