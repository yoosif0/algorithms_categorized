"""
https://leetcode.com/problems/find-peak-element
#binary_search
didn't add padding on left and right because time would be O(n) instead of O(log n)
"""

import unittest


class Solution:
    def findPeakElement(self, a: list[int]) -> int:
        if len(a) == 1:
            return 0
        if a[0] > a[1]:
            return 0
        if a[-1] > a[-2]:
            return len(a) - 1
        l = 1
        r = len(a) - 2
        while l <= r:
            m = (l + r) // 2
            if a[m] < a[m + 1]:
                l = m + 1
            elif a[m] < a[m - 1]:
                r = m - 1
            else:
                return m


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findPeakElement([1, 2, 1, 3, 5, 6, 4]), 5)


if __name__ == "__main__":
    unittest.main()
