"""
https://leetcode.com/problems/container-with-most-water/description/
[1,5,1,2,5,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3,20,6,3]
minimum height is the limiting factor so we can move the pointer pointing to shorter heights
"""

import unittest


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            cur_area = min(height[l], height[r]) * (r - l)
            ans = max(ans, cur_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(t.maxArea([1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
