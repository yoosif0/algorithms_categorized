"""
@nested-tags:greedy/constructive,knapsack/fractional
https://leetcode.com/problems/maximum-units-on-a-truck
"""

import unittest


class Solution:
    def maximumUnits(self, a: list[list[int]], t: int) -> int:
        a.sort(key=lambda x: -x[1])
        ans = 0
        for i in range(len(a)):
            if t <= a[i][0]:
                ans += a[i][1] * t
                break
            t -= a[i][0]
            ans += a[i][1] * a[i][0]
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maximumUnits([[1, 3], [2, 2], [3, 1]], 4), 8)


if __name__ == "__main__":
    unittest.main()
