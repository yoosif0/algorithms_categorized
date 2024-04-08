"""
https://leetcode.com/problems/insert-delete-getrandom-o1

main idea: swap elements in array with last element before popping so that popping the element takes O(1) time
#swpd
#store_index

9 12 90 r9 134 1 339 9238 19 91 2 3 389 2 2 33 2

m:{9:0 12:1, 90:2}
a:[9,12,90]


"""

import random
import unittest


class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.a = []

    def insert(self, x: int) -> bool:
        if x in self.m:
            return False
        self.a.append(x)
        self.m[x] = len(self.a) - 1
        return True

    def remove(self, x: int) -> bool:
        if x not in self.m:
            return False
        # swap with last element and update "m" accordingly
        swp_val, x_i = self.a[-1], self.m[x]
        self.m[swp_val] = x_i
        self.a[x_i] = swp_val
        # remove x from "m" and "a"
        del self.m[x]
        self.a.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.a)


class Test(unittest.TestCase):
    def test(self):
        # ["i","i","i","i","i","g","i","r","i","i"]
        # [[1],[-2],[-2],[-2],[1],[],[-2],[0],[-3],[1]]
        t = RandomizedSet()
        t.insert(3)
        t.insert(-2)
        t.remove(2)
        t.insert(1)
        t.insert(-3)
        t.insert(-2)
        t.remove(-2)
        t.remove(3)
        t.insert(-1)
        t.remove(-3)
        # print(t.getRandom())
        # t.remove(0)


if __name__ == "__main__":
    unittest.main()
