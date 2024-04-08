"""
https://leetcode.com/problems/random-flip-matrix
#grid
"""

import random
import unittest


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.flp = {}
        self.reset()

    def flip(self) -> list[int]:
        i = random.randint(0, self.ttl - 1)
        x = self.flp.get(i, i)
        self.ttl -= 1
        self.flp[i] = self.flp.get(self.ttl, self.ttl)
        self.flp[self.ttl] = x
        print("log")
        print("i", i)
        print("x", x)
        print(self.flp)
        print(self.ttl)
        return [x // self.n, x % self.n]

    def reset(self) -> None:
        self.ttl = self.m * self.n


class Test(unittest.TestCase):
    def test(self):
        t = Solution(50, 2)
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        print(t.flip())
        t.reset()
        print(t.flip())


if __name__ == "__main__":
    unittest.main()
