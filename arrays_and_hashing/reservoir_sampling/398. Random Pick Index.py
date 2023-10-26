"""
https://leetcode.com/problems/random-pick-index
"""
from collections import defaultdict
import random
import unittest


class Solution:
    def __init__(self, a: list[int]):
        self.m = defaultdict(list)
        for i in range(len(a)):
            self.m[a[i]].append(i)

    def pick(self, x) -> int:
        return random.choice(self.m[x])


class Test(unittest.TestCase):
    def test(self):
        t = Solution([1, 2, 3, 3, 3])
        print(t.pick(1))
        print(t.pick(1))
        print(t.pick(1))
        print(t.pick(2))
        print(t.pick(2))
        print(t.pick(3))
        print(t.pick(3))
        print(t.pick(3))
        print(t.pick(3))


if __name__ == "__main__":
    unittest.main()
