"""
https://leetcode.com/problems/binary-search/
"""

import unittest
import bisect


class Solution:
    def search(self, a: list[int], t: int) -> int:
        i = bisect.bisect_left(a, t)
        return i if i < len(a) and a[i] == t else -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(t.search([-1, 0, 3, 5, 9, 12], 2), -1)
        self.assertEqual(t.search([2, 5], 5), 1)


if __name__ == "__main__":
    unittest.main()
