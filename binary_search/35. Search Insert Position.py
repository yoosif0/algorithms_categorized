"""
@nested-tags:binary_search/remove_from_l
https://leetcode.com/problems/search-insert-position/

You need to remove from l because if the target is found, you need to return the target index
"""

import unittest


class Solution:
    def searchInsert(self, a: list[int], t: int) -> int:
        l = 0
        r = len(a)
        while l < r:
            mid = (l + r) // 2
            if a[mid] < t:
                l = mid + 1
            else:
                r = mid
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
