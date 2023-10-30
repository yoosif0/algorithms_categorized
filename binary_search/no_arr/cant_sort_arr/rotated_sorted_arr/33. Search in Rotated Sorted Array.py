"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Search for the pivot (minIndex which I already solved before). See if the target is to the right or left of the 
pivot by comparing the target to the right most value. If it's larger than it so the target is on the 
left portion. If not then it's in the right portion. Then we do a binary search on the correct portion.
Remember to add the missed indecis to the result if you searched the right portion.

#both_right_left_works
#differet_l_r

"""

import bisect
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
        return l

    def search(self, a: list[int], t: int) -> int:
        i = self.findMin(a)
        ans = (
            bisect.bisect_left(a, t, 0, i)
            if t > a[-1]
            else bisect.bisect_left(a, t, i, len(a))
        )
        return ans if ans < len(a) and a[ans] == t else -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.search([4, 5, 6, 7, 0, 1, 2], 4), 0)
        self.assertEqual(t.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(t.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(t.search([1], 1), 0)
        self.assertEqual(t.search([1, 3], 3), 1)
        self.assertEqual(t.search([3, 1], 3), 0)


if __name__ == "__main__":
    unittest.main()