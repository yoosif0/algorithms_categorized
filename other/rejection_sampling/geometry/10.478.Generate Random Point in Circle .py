"""
#math
#distance_point
https://leetcode.com/problems/generate-random-point-in-a-circle
"""

from math import sqrt
import random
import unittest


class Solution:
    def __init__(self, r: float, x: float, y: float):
        self.r = r
        self.x = x
        self.y = y

    def randPoint(self) -> list[float]:
        while True:
            x = random.uniform(self.x - self.r, self.x + self.r)
            y = random.uniform(self.y - self.r, self.y + self.r)
            if sqrt((x - self.x) ** 2 + (y - self.y) ** 2) <= self.r:
                return [x, y]


class Test(unittest.TestCase):
    def test(self):
        t = Solution(1, 0, 0)
        N = 100
        for _ in range(N):
            p = t.randPoint()
            print(p)


if __name__ == "__main__":
    unittest.main()
