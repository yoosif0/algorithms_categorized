"""
https://leetcode.com/problems/search-insert-position/
it's flexible because the arr have distinct values
"""

import unittest


class Solution:
    def searchInsert(self, a: list[int], t: int) -> int:
        l = 0
        r = len(a)
        while l < r:
            m = (l + r) // 2
            if a[m] < t:
                l = m + 1
            elif a[m] > t:
                r = m
            else:
                return m
        return l


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(t.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(t.searchInsert([1, 3, 5, 6], 0), 0)
        self.assertEqual(t.searchInsert([1, 3], 2), 1)


if __name__ == "__main__":
    unittest.main()
