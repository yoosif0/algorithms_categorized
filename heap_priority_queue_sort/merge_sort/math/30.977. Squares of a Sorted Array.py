"""
https://leetcode.com/problems/squares-of-a-sorted-array/
#math

like "simplest" 

The trick here is that this looks like a parabola with a valley. The max value is in one of both ends of array.
"""

import unittest


# O(n) time and O(n) space
class Solution:
    def sortedSquares(self, a: list[int]) -> list[int]:
        l = 0
        r = len(a) - 1
        a = [n**2 for n in a]
        ans = [None for _ in range(len(a))]
        for i in range(len(ans) - 1, -1, -1):
            if a[r] > a[l]:
                ans[i] = a[r]
                r -= 1
            else:
                ans[i] = a[l]
                l += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(t.sortedSquares([-5, -3, -2, -1]), [1, 4, 9, 25])


if __name__ == "__main__":
    unittest.main()
