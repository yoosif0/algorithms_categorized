"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
#first_occurrence
"""

import unittest


class Solution:
    def findMin(self, a: list[int]) -> int:
        l = 0
        r = len(a) - 1
        while l < r:
            m = (l + r) // 2
            # the line below holds the whole trick that differentiatest this problem from 153. Find Min...
            if a[m] > a[r]:
                l = m + 1
            elif a[m] < a[r]:
                r = m
            else:
                r -= 1
        return a[l]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findMin([0, 0, 0, 1, 0]), 0)
        self.assertEqual(t.findMin([3, 3, 3, 3, 3, 3, 1, 3]), 1)
        self.assertEqual(t.findMin([3, 1, 3, 3, 3, 3, 3, 3]), 1)
        self.assertEqual(t.findMin([1, 3, 5]), 1)
        self.assertEqual(t.findMin([2, 2, 2, 0, 1]), 0)
        self.assertEqual(t.findMin([2, 0, 0, 1, 2]), 0)
        self.assertEqual(t.findMin([3, 3, 1, 3]), 1)
        self.assertEqual(t.findMin([1, 3, 3]), 1)


if __name__ == "__main__":
    unittest.main()
