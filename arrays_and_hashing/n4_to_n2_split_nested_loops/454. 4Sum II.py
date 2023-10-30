"""
https://leetcode.com/problems/4sum/
The main gist here is that we can use 2 double nested loops instead of 1 quadritic nested loop
and use storage to reduce our complexity from something very slow like O(n^4) to O(n^2)
"""


import collections
import unittest


class Solution:
    def fourSumCount(
        self, a1: list[int], a2: list[int], a3: list[int], a4: list[int]
    ) -> int:
        m = collections.Counter()
        ans = 0
        for i in range(len(a1)):
            for j in range(len(a1)):
                m[a1[i] + a2[j]] += 1
        for i in range(len(a1)):
            for j in range(len(a1)):
                ans += m[-a3[i] - a4[j]]
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]), 2)


if __name__ == "__main__":
    unittest.main()
