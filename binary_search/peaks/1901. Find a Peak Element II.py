"""
https://leetcode.com/problems/find-a-peak-element-ii/
#binary_search
#matrix


10 21 15 22 34 18
21 30 14 25  9 10
 7 16 32 35 10 20
22 29 15 28 19 12

30, 35, 29, 34, 20
"""

import unittest


class Solution:
    def findPeakGrid(self, g: list[list[int]]) -> list[int]:
        pass


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.findPeakGrid([[10, 20, 15], [21, 30, 14], [7, 16, 32]]), [1, 1]
        )
        self.assertEqual(t.findPeakGrid([[1, 4], [3, 2]]), [0, 1])


if __name__ == "__main__":
    unittest.main()
