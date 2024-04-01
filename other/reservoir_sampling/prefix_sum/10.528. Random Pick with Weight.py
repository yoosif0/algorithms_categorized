"""
https://leetcode.com/problems/random-pick-with-weight/

6,2,10,1,3,2,3
"""

import bisect
from itertools import accumulate
import random
import unittest


class Solution:
    def __init__(self, a: list[list[int]]):
        pre = list(accumulate(a))
        self.a = a
        self.pre = pre

    def pickIndex(self) -> int:
        rnd = random.randint(1, self.pre[-1])
        return bisect.bisect_left(self.pre, rnd)


class Test(unittest.TestCase):
    def test(self):
        t = Solution([1, 3])
        N = 100000
        cur = 0
        for _ in range(N):
            i = t.pickIndex()
            if i == 0:
                cur += 1
        print(cur / N)


if __name__ == "__main__":
    unittest.main()
