"""
https://leetcode.com/problems/find-the-highest-altitude/

"""
from itertools import accumulate
import unittest


class Solution:
    def largestAltitude(self, a: list[int]) -> int:
        ans = max(list(accumulate(a, initial=0)))
        # we can't fall below 0 (hence the max)
        return max(0, ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.largestAltitude([-5, 1, 5, 0, -7]), 1)


if __name__ == "__main__":
    unittest.main()
