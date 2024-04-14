"""
https://leetcode.com/problems/binary-subarrays-with-sum

We can use sliding window because the condition is monotonic
"""

import collections
from itertools import accumulate
import unittest


class Solution:
    def numSubarraysWithSum(self, a: list[int], k: int) -> int:
        m = {0: 1}
        cnt = 0
        cur = 0
        for r in range(len(a)):
            cur += a[r]
            if cur - k in m:
                cnt += m[cur - k]
            if cur not in m:
                m[cur] = 0
            m[cur] += 1
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numSubarraysWithSum([1, 0, 1, 0, 1], 2), 4)
        self.assertEqual(t.numSubarraysWithSum([0, 0, 0, 0, 0], 0), 15)


if __name__ == "__main__":
    unittest.main()
