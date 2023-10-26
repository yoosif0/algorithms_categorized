"""
https://leetcode.com/problems/sort-colors/
"""

import collections
import unittest


class Solution:
    def sortColors(self, a: list[int]) -> None:
        bs = collections.Counter(a)
        j = 0
        for i in range(0, 3):
            for _ in range(bs[i]):
                a[j] = i
                j += 1
        return a


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sortColors([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])


if __name__ == "__main__":
    unittest.main()
