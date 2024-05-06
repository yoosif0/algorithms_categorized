"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
Search for the pivot (minIndex which I already solved before). See if the target is to the right or left of the 
pivot by comparing the target to the right most value. If it's larger than it so the target is on the 
left portion. If not then it's in the right portion. Then we do a binary search on the correct portion.
Remember to add the missed indecis to the result if you searched the right portion.

#both_right_left_works
#differet_l_r

"""

import unittest


class Solution:
    def search(self, a: list[int], t: int) -> int:
        # find min (pivot point)
        l = 0
        r = len(a) - 1
        while l < r:
            m = (l + r) // 2
            if a[m] > a[r]:
                l = m + 1
            else:
                r = m
        pvt = l
        if t > a[-1]:
            l = 0
            r = pvt - 1
        elif t < a[-1]:
            l = pvt
            r = len(a) - 1
        else:
            return len(a) - 1
        while l <= r:
            m = (l + r) // 2
            if a[m] < t:
                l = m + 1
            elif a[m] > t:
                r = m - 1
            else:
                return m
        return -1


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
