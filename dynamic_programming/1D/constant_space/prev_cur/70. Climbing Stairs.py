"""
https://leetcode.com/problems/climbing-stairs/
4

2 2
2 1 1
1 2 1
1 1 2
1 1 1 1

#count_combination
#prev_cur
#optimal_substructure
#overlapping_subproblems
#recursion
"""


import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 1
        for _ in range(2, n + 1):
            prev, cur = cur, cur + prev
        return cur


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.climbStairs(2), 2)
        self.assertEqual(t.climbStairs(3), 3)
        self.assertEqual(t.climbStairs(4), 5)


if __name__ == "__main__":
    unittest.main()
