"""
https://leetcode.com/problems/find-the-middle-index-in-array/
if what's on the right of the pivot equals to what's on the right
same as 724
"""
from itertools import accumulate
import unittest


class Solution:
    def findMiddleIndex(self, a: list[int]) -> int:
        dp = list(accumulate(a, initial=0))
        for i in range(1, len(dp)):
            if dp[-1] - dp[i] == dp[i - 1]:
                return i - 1
        return -1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.findMiddleIndex([2, 3, -1, 8, 4]), 3)


if __name__ == "__main__":
    unittest.main()
