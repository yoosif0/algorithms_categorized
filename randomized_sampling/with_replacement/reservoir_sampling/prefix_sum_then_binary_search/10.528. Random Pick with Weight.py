"""
https://leetcode.com/problems/random-pick-with-weight/
"""

from itertools import accumulate
import random
import unittest


class Solution:
    def __init__(self, a: list[list[int]]):
        pre = list(accumulate(a))
        self.wps = pre

    def pickIndex(self) -> int:
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
        return l


"""
112 437 5
112 549 554

t = 200.23
"""


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
