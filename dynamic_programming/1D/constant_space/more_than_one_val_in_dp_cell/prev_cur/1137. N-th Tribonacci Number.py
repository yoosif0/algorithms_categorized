"""
https://leetcode.com/problems/fibonacci-number/
#pre_cur
"""

import unittest


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        vpre, pre, cur = 0, 1, 1
        for _ in range(3, n + 1):
            vpre, pre, cur = pre, cur, vpre + pre + cur
        return cur


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.tribonacci(4), 4)
        self.assertEqual(t.tribonacci(25), 1389537)


if __name__ == "__main__":
    unittest.main()
