"""
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles
#integer_points : like area but add 1 to each dimention (width and length)
"""

import random
import unittest


class Solution:
    def __init__(self, a: list[list[int]]):
        # weight distribution for each rectanlge (like area but add 1 since outer points are included)
        acc = 0
        wps = []
        for i in range(len(a)):
            acc += (a[i][2] - a[i][0] + 1) * (a[i][3] - a[i][1] + 1)
            wps.append(acc)
        self.a = a
        self.wps = wps

    def pick(self) -> int:
        t = random.uniform(0, self.wps[-1])
        # find index of first item greater than t
        l = 0
        r = len(self.wps) - 1
        while l < r:
            m = (l + r) // 2
            if self.wps[m] < t:
                l = m + 1
            else:
                r = m
        rect = self.a[l]
        # now pick a random point in the picked rectangle
        return [
            random.randint(rect[0], rect[2]),
            random.randint(rect[1], rect[3]),
        ]


class Test(unittest.TestCase):
    def test(self):
        t = Solution(
            [
                [10, 9, 11, 12],
                [0, 0, 2, 1],
                [-2, -2, 1, 1],
                [2, 2, 6, 5],
            ]
        )
        print(t.pick())
        print(t.pick())
        print(t.pick())
        print(t.pick())
        print(t.pick())
        print(t.pick())
        print(t.pick())
        print(t.pick())
        print(t.pick())


if __name__ == "__main__":
    unittest.main()
