"""
https://leetcode.com/problems/subarray-sum-equals-k/

We here also can't use sliding window because the condition is monotonic
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
        cur = 0
        ans = 0
        m = {0: 1}
        for i in range(len(a)):
            cur += a[i]
            if cur - k in m:
                ans += m[cur - k]
            m[cur] = m.get(cur, 0) + 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.subarraySum([1, 2, 8, 1, 2, 0, -5, 1], 10), 2)
        self.assertEqual(t.subarraySum([1, 1, 1], 2), 2)


if __name__ == "__main__":
    unittest.main()
