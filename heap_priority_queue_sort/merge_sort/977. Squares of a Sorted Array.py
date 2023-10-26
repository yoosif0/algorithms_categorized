"""
https://leetcode.com/problems/squares-of-a-sorted-array/

The idea here is that the 2 extremes of left and right have the highest absolute numbers. This means
we don't need to fully sort. We can have 2 pointers and compare whichever is higher, add the result to the
end of the result array

#math
the math concept here is that this acts as if you have 2 sorted arrays since square of a negative value with high magnitue at the beginning is a high value
"""

import unittest


# O(n) time and O(n) space
class Solution:
    def sortedSquares(self, a: list[int]) -> list[int]:
        l = 0
        r = len(a) - 1
        ans = [None for _ in range(len(a))]
        for i in range(len(ans) - 1, -1, -1):
            if abs(a[r]) > abs(a[l]):
                ans[i] = pow(a[r], 2)
                r -= 1
            else:
                ans[i] = pow(a[l], 2)
                l += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(t.sortedSquares([-5, -3, -2, -1]), [1, 4, 9, 25])


if __name__ == "__main__":
    unittest.main()
