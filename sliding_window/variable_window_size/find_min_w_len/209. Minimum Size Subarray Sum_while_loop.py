"""
https://leetcode.com/problems/minimum-size-subarray-sum/

[2,3,1,2,4,3]
Window 2
2 3  s5
231 s6
2312 s8 yes a4 s6 l1
3124 s7 yes a4 s7 


[1,1,1,1,4,3]
[1,2,3,4,8,11]

"""


import unittest
import sys


class Solution:
    def minSubArrayLen(self, target: int, a: list[int]):
        ans = sys.maxsize
        l = 0
        w = 0
        for r in range(len(a)):
            w += a[r]
            while w >= target:
                ans = min(r - l + 1, ans)
                # try to shift l to the right as much as possible
                w -= a[l]
                l += 1
        return 0 if ans == sys.maxsize else ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)
        self.assertEqual(t.minSubArrayLen(4, [1, 4, 4]), 1)
        self.assertEqual(t.minSubArrayLen(14, [1, 1, 1, 1, 1, 1, 1, 1]), 0)
        self.assertEqual(t.minSubArrayLen(9, [2, 3, 1, 2, 4, 2, 6, 3]), 2)
        self.assertEqual(t.minSubArrayLen(15, [1, 2, 3, 4, 5]), 5)


if __name__ == "__main__":
    unittest.main()
