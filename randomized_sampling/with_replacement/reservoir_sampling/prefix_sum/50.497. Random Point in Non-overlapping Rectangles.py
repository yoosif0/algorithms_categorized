"""
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles
#integer_points : like area but add 1 to each dimention (width and length)
#prefix_sum : prefix sum makes it easier to create sampling pool
#bisect
"""

import bisect
import random
import unittest


class Solution:
    def __init__(self, a: list[list[int]]):
        cur = 0
        pre = []
        for x in a:
            # like area but add 1 since we want integer points
            cur += (x[2] - x[0] + 1) * (x[3] - x[1] + 1)
            pre.append(cur)
        self.a = a
        self.pre = pre

    def pick(self) -> int:
        x = random.randint(0, self.pre[-1])
        i = bisect.bisect_left(self.pre, x)
        k = self.a[i]
        return [
            random.randint(k[0], k[2]),
            random.randint(k[1], k[3]),
        ]


class Test(unittest.TestCase):
    def test(self):
        t = Solution(
            [
                [53487036, -14015982, 53487038, -14015981],
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
