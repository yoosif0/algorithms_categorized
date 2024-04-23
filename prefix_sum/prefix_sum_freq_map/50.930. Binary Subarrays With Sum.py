"""
https://leetcode.com/problems/binary-subarrays-with-sum

We can use sliding window because the condition is monotonic
"""

import unittest


class Solution:
    def numSubarraysWithSum(self, a: list[int], k: int) -> int:
        m = {0: 1}
        cnt = 0
        acc = 0
        for i in range(len(a)):
            acc += a[i]
            if acc - k in m:
                cnt += m[acc - k]
            if acc not in m:
                m[acc] = 0
            m[acc] += 1
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.numSubarraysWithSum([1, 0, 1, 0, 1], 2), 4)
        self.assertEqual(t.numSubarraysWithSum([0, 0, 0, 0, 0], 0), 15)


if __name__ == "__main__":
    unittest.main()
