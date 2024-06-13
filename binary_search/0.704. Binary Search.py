"""
https://leetcode.com/problems/binary-search/
"""

import unittest


class Solution:
    def search(self, a: list[int], t: int) -> int:
        l = 0
        r = len(a) - 1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] < t:
                l = mid + 1
            elif a[mid] > t:
                r = mid - 1
            else:
                return mid
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(t.search([-1, 0, 3, 5, 9, 12], 2), -1)
        self.assertEqual(t.search([2, 5], 5), 1)


if __name__ == "__main__":
    unittest.main()
