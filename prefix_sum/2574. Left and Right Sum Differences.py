"""
@nested-tags:prefix_sum/subarray
https://leetcode.com/problems/left-and-right-sum-differences/
"""

from itertools import accumulate
import unittest


class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        ans = [0 for _ in range(len(a))]
        a = list(accumulate(a, initial=0))
        for i in range(len(ans)):
            ans[i] = abs(a[-1] - a[i + 1] - a[i])
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.leftRightDifference([10, 4, 8, 3]), [15, 1, 11, 22])


if __name__ == "__main__":
    unittest.main()
