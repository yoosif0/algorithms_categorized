"""
https://leetcode.com/problems/h-index/
"""

import collections
import unittest


class Solution:
    def hIndex(self, a: list[int]) -> int:
        # counting sort
        cnt = collections.Counter(a)
        mx = max(a)
        a2 = []
        for i in range(0, mx + 1):
            a2.extend([i] * cnt[i])
        a = a2
        l = 0
        r = len(a)
        while l < r:
            m = (l + r) // 2
            if a[m] < len(a) - m:
                l = m + 1
            else:
                r = m
        return len(a) - l


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.hIndex([0, 1, 3, 5, 6]), 3)
        self.assertEqual(t.hIndex([1, 1, 3]), 1)
        self.assertEqual(t.hIndex([100]), 1)
        self.assertEqual(t.hIndex([11, 15]), 2)
        self.assertEqual(t.hIndex([0, 0, 4, 4]), 2)


if __name__ == "__main__":
    unittest.main()
