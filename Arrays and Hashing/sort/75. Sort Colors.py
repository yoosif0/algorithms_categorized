"""
https://leetcode.com/problems/sort-colors/
#sort
sorting between a constant relatively small number of possibilities. in place
"""

import unittest


# 2 passes O(n) time. O(1) space
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # Count colors
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        # fill colors in nums array from 0 to 2
        i = 0
        for j in range(3):
            for _ in range(count[j]):
                nums[i] = j
                i += 1
        return nums


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sortColors([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])


if __name__ == "__main__":
    unittest.main()
