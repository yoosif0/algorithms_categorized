"""
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
#store_index
#store_indecis
"""

from collections import defaultdict
import random
import unittest


class RandomizedCollection:

    def __init__(self):
        self.m: dict[int, set[int]] = defaultdict(set)
        self.a: list[int] = []

    def insert(self, x: int) -> bool:
        fl = len(self.m[x]) == 0
        self.a.append(x)
        self.m[x].add(len(self.a) - 1)
        return fl

    def remove(self, x: int) -> bool:
        if len(self.m[x]) == 0:
            return False
        # swap with last element and update "m" accordingly
        swp_val, x_i = self.a[-1], self.m[x].pop()
        self.m[swp_val].add(x_i)
        self.m[swp_val].remove(len(self.a) - 1)
        self.a[x_i] = swp_val
        self.a.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.a)


class Test(unittest.TestCase):
    def test(self):
        t = RandomizedCollection()
        t.insert(1)
        t.insert(1)
        t.insert(2)
        print(t.getRandom())
        t.remove(1)
        print(t.getRandom())


if __name__ == "__main__":
    unittest.main()
