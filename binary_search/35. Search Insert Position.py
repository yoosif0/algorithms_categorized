"""
https://leetcode.com/problems/search-insert-position/
"""


import unittest


class Solution:
    def searchInsert(self, a: list[int], target: int) -> int:
        l = 0
        r = len(a)
        while l < r:
            m = (r + l) // 2
            if a[m] < target:
                l = m + 1
            else:
                r = m
        return l


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(t.searchInsert([1, 3, 5, 6], 7), 4)


if __name__ == "__main__":
    unittest.main()
