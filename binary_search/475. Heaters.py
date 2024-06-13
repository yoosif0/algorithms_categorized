"""
@nested-tags:binary_search/lhs_rhs
https://leetcode.com/problems/heaters

Input: houses = [1,2,3,4], heaters = [1,4,5]

"""

import sys
import unittest


class Solution:
    def findRadius(self, a: list[int], a2: list[int]) -> int:
        a.sort()
        a2.sort()

        # RHS
        nr = [sys.maxsize for _ in range(len(a))]
        for i in range(len(a)):
            l = 0
            r = len(a2)
            t = a[i]
            while l < r:
                mid = (l + r) // 2
                if a2[mid] < t:
                    l = mid + 1
                else:
                    r = mid
            if l < len(a2):
                nr[i] = a2[l] - t

        # LHS
        nl = [sys.maxsize for _ in range(len(a))]
        for i in range(len(a)):
            l = -1
            r = len(a2) - 1
            t = a[i]
            while l < r:
                mid = (l + r + 1) // 2
                if a2[mid] > t:
                    r = mid - 1
                else:
                    l = mid
            if l != -1:
                nl[i] = t - a2[l]

        # min of LHS and RHS
        a = [min(nl[i], nr[i]) for i in range(len(nl))]
        # return farthest
        return max(a)


"""
5,8,10,12,13,14,63        3,11,18,20,30
nr = [6, 3, 1, 6, 5, 6, maxsize]
nl = []
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.findRadius([5, 8, 10, 12, 13, 14, 63], [3, 11, 18, 20, 30]), 33
        )
        self.assertEqual(t.findRadius([1, 2, 3], [2]), 1)
        self.assertEqual(t.findRadius([1, 2, 3, 4], [1, 4]), 1)
        self.assertEqual(t.findRadius([1, 5], [2]), 3)


if __name__ == "__main__":
    unittest.main()
