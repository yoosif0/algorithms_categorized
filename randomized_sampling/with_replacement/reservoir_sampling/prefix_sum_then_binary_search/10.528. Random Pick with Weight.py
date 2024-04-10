"""
https://leetcode.com/problems/random-pick-with-weight/
#bisect_post_process
6,2,10,1,3,2,3
"""

import bisect
from itertools import accumulate
import random
import unittest


class Solution:
    def __init__(self, a: list[list[int]]):
        pre = list(accumulate(a, initial=0))
        self.pre = pre

    def pickIndex(self) -> int:
        rnd = random.uniform(0, self.pre[-1])
        return bisect.bisect_left(self.pre, rnd) - 1


class Test(unittest.TestCase):
    def test(self):
        t = Solution([1, 3])
        N = 100000
        cur = 0
        for _ in range(N):
            i = t.pickIndex()
            print(i)
            if i == 0:
                cur += 1
        print(cur / N)


if __name__ == "__main__":
    unittest.main()
