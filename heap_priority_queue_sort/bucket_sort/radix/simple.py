"""
"""

import unittest


def digit(n: int, digit_order: int):
    r = None
    for _ in range(digit_order):
        r = n % 10
        n = n // 10
    return r


class Solution:
    def radix(self, a: list[int]) -> bool:
        BASE = 10
        for i in range(6):
            sub = [[] for _ in range(BASE)]
            for n in a:
                sub[digit(n, i + 1)].append(n)
            a = []
            for arr in sub:
                for x in arr:
                    a.append(x)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        t.radix([5, 213, 55, 21, 31, 20, 430])
        self.assertEqual(digit(13, 2), 1)
        self.assertEqual(digit(213, 2), 1)


if __name__ == "__main__":
    unittest.main()
