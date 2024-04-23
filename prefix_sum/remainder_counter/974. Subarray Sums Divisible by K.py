"""
https://leetcode.com/problems/subarray-sums-divisible-by-k
"""

import collections
from itertools import accumulate
import unittest


class Solution:
    def subarraysDivByK(self, a: list[int], k: int) -> int:
        a = list(accumulate(a, initial=0))
        m = collections.Counter()
        cnt = 0
        for i in range(len(a)):
            rm = a[i] % k
            cnt += m[rm]
            m[rm] += 1
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.subarraysDivByK([4, 5, 0, -2, -3, 1], 5), 7)
        self.assertEqual(t.subarraysDivByK([5], 9), 0)


if __name__ == "__main__":
    unittest.main()
