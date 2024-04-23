"""
https://leetcode.com/problems/subarray-sum-equals-k/

We here also can't use sliding window because the condition is NOT monotonic
#subarr
Input: nums = [1,2,8,1,2,0,-5,1], k = 10
1: save 1
2: save 3; we don't have -7 saved
8: save 11; we have 1 saved so total++
1: save 12; we don't have 2
2: save 14; we don't have 4
0: save 14 again; we don't have 4
-5:save 9; we don't have -1
1: save 10; we don't have 0 total++
"""

import unittest


class Solution:
    def subarraySum(self, a: list[int], k: int) -> int:
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
        self.assertEqual(t.subarraySum([1, 2, 8, 1, 2, 0, -5, 1], 10), 2)
        self.assertEqual(t.subarraySum([1, 1, 1], 2), 2)
        self.assertEqual(t.subarraySum([-1, -1, 1], 0), 1)


if __name__ == "__main__":
    unittest.main()
