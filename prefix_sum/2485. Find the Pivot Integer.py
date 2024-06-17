"""
@nested-tags:prefix_sum/subarray
https://leetcode.com/problems/find-the-pivot-integer/
"""

from itertools import accumulate
import unittest


class Solution:
    def pivotInteger(self, n: int) -> int:
        a = [i for i in range(n + 1)]
        a = list(accumulate(a))
        for i in range(1, len(a)):
            # sum of values on the left is a[i-1] and on the right is a[-1] - a[i]
            if a[i - 1] == a[-1] - a[i]:
                return i
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.pivotInteger(8), 6)
        self.assertEqual(t.pivotInteger(1), 1)
        self.assertEqual(t.pivotInteger(4), -1)


if __name__ == "__main__":
    unittest.main()
