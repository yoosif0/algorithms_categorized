"""
https://leetcode.com/problems/container-with-most-water/
[1,5,1,2,5,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3,20,6,3]
minimum height is the limiting factor so we can move the pointer pointing to shorter heights

[1,8,6,2,5,4,8,3,7]
1,8: 2
1,8,6:2  since r<l we shrink l
8,6:6
8,6,2:4
8,6,2,5:15
8,6,2,5,4:16
8,6,2,5,4,8:40
8,6,2,5,4,8,3:18
8,6,2,5,4,8,3,7:49
"""

import unittest


class Solution:
    def maxArea(self, a: list[int]) -> int:
        l = 0
        r = len(a) - 1
        bst = 0
        while l < r:
            cur = min(a[l], a[r]) * (r - l)
            bst = max(bst, cur)
            if a[l] < a[r]:
                l += 1
            else:
                r -= 1
        return bst


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(t.maxArea([1, 1]), 1)
        self.assertEqual(t.maxArea([1, 2, 1]), 2)


if __name__ == "__main__":
    unittest.main()
