"""
https://leetcode.com/problems/4sum/
The main gist here is that we can use 2 double nested loops instead of 1 quadritic nested loop
and use storage to reduce our complexity from something very slow like O(n^4) to O(n^2)
"""


import unittest
from collections import defaultdict


class Solution:
    def fourSumCount(
        self, a1: list[int], a2: list[int], a3: list[int], a4: list[int]
    ) -> int:
        targets = defaultdict(lambda: 0)
        ans = 0
        length = len(a1)
        for i in range(length):
            for j in range(length):
                partial_sum = a1[i] + a2[j]
                targets[partial_sum] += 1
        for i in range(length):
            for j in range(length):
                partial_sum = a3[i] + a4[j]
                ans += targets[-partial_sum]
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]), 2)


if __name__ == "__main__":
    unittest.main()
