import functools
import unittest

"""
4::::::::::::::::
1111
121
211

112
22




5::::::::::::::::
11111
1211
2111
1121
221

122
212
1112

"""


class Solution:
    @functools.lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.climbStairs(1), 1)
        self.assertEqual(t.climbStairs(2), 2)
        self.assertEqual(t.climbStairs(3), 3)
        self.assertEqual(t.climbStairs(4), 5)
        self.assertEqual(t.climbStairs(5), 8)
        self.assertEqual(t.climbStairs(6), 13)


if __name__ == "__main__":
    unittest.main()
