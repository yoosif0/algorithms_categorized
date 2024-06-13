"""
@nested-tags:binary_search/remove_from_l,binary_search/first_occurance,binary_search/rotated_sorted_arr
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
"""

import unittest


class Solution:
    def findMin(self, a: list[int]) -> int:
        l = 0
        r = len(a) - 1
        while l < r:
            mid = (l + r) // 2
            if a[mid] > a[r]:
                l = mid + 1
            elif a[mid] < a[r]:
                r = mid
            # the line below holds the whole trick that differentiatest this problem from 153. Find Min...
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
