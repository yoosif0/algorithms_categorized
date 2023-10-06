"""
https://leetcode.com/problems/integer-break/
10
9 1 10
8 2 16
7 3 21
6 4 24
5 5 25
5 5
--
4 5 1 20
3 3 4 36
-------------------------
9
8 1 8
7 2 14
6 3 18
3 4 2 24
3 3 3 27

just reduce to prime numbers and try to have 3 in there??
-----------
8
3 3 2 18
--------
7 
3 4 12
----
3
3 
-----
6
3 3
----
5
2 3
---
I just tried different patterns to come up with the solution. No use of proof
"""
import unittest


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        threes = n // 3
        twos = 0
        remainder = n % 3
        if remainder == 1:
            threes -= 1
            twos += 2
        if remainder == 2:
            twos += 1
        return pow(3, threes) * pow(2, twos)


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.integerBreak(2), 1)
        self.assertEqual(t.integerBreak(10), 36)
        self.assertEqual(t.integerBreak(3), 2)
        self.assertEqual(t.integerBreak(5), 6)
        self.assertEqual(t.integerBreak(6), 9)


if __name__ == "__main__":
    unittest.main()
