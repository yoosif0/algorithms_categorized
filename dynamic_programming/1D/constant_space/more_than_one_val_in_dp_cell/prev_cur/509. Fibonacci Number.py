"""
https://leetcode.com/problems/fibonacci-number/
#pre_cur
"""

import unittest


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        pre, cur = 0, 1
        for _ in range(2, n + 1):
            pre, cur = cur, pre + cur
        return cur


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.fib(4), 3)


if __name__ == "__main__":
    unittest.main()
