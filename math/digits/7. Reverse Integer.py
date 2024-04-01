"""
https://leetcode.com/problems/reverse-integer
"""

import unittest


class Solution:
    def reverse(self, n: int) -> int:
        # fl is whether n is negative
        fl = n < 0
        # strip negative sign if exists
        n = abs(n)
        ans = 0
        while n:
            ans = ans * 10 + n % 10
            n //= 10
        if ans > +(2**31) or ans < -(2**31):
            return 0
        return -ans if fl else ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.reverse(121), 121)
        self.assertEqual(t.reverse(123), 321)
        self.assertEqual(t.reverse(-123), -321)
        self.assertEqual(t.reverse(1534236469), 0)


if __name__ == "__main__":
    unittest.main()
