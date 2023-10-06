"""
https://leetcode.com/problems/min-cost-climbing-stairs
 10        15       20 
[10,0],  [25,15]   [10+20, 15]   

          [1,    100,      1,   1,1,100,  1, 1, 100,1]
0   0      1      100      2    3 3 103   4  5  104,6

dp[i] = val + min(i-1, i-2)


#optimization
#prev_cur
"""


import unittest


class Solution:
    def minCostClimbingStairs(self, a: list[int]) -> int:
        prev, cur = 0, 0
        for i in range(len(a)):
            prev, cur = cur, min(cur, prev) + a[i]
        return min(cur, prev)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(
            t.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6
        )
        self.assertEqual(t.minCostClimbingStairs([2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
