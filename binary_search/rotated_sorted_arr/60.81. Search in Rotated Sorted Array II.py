"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
cant make binary search O(log n) since there are repeated elements
"""

import unittest


class Solution:
    def search(self, a: list[int], t: int) -> int:
        for n in a:
            if n == t:
                return True
        return False


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.search([4, 5, 6, 0, 0, 1, 2], 0), True)
        self.assertEqual(
            t.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2),
            True,
        )


if __name__ == "__main__":
    unittest.main()
