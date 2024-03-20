"""
https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors
"""

import unittest


class Solution:
    def maxConsecutive(self, l: int, h: int, a: list[int]) -> int:
        a.sort() 
        ans = 0
        for i in range(1, len(a)):
            ans = max(ans, a[i] - a[i-1] -1)
        # just make sure lo and hi don't have the max gap
        ans = max(ans, a[0]-l, h- a[-1])
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxConsecutive(2,9,[4,6]), 3)
        self.assertEqual(t.maxConsecutive(6,8,[7,6,8]), 0)


if __name__ == "__main__":
    unittest.main()

