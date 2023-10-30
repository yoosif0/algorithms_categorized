"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
3, 4, 5, 1, 2
4, 5, 6, 7, 0, 1, 2
#both_right_left_works
"""
import unittest


class Solution:
    def findMin(self, a: list[int]) -> int:
        l = 0
        r = len(a) - 1
        while l < r:
            m = (l + r) // 2
            if a[m] > a[r]:
                l = m + 1
            else:
                r = m
        return a[l]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(t.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(t.findMin([11, 13, 15, 17]), 11)
        self.assertEqual(t.findMin([3, 1, 2]), 1)


if __name__ == "__main__":
    unittest.main()