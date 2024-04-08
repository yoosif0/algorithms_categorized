"""
https://leetcode.com/problems/shuffle-an-array/
[1,2,3]
pick one random from arr and append to new_arr. to remove the picked element, switch it with last in a and a.pop()
[]
#in_place
"""

import random
import unittest


class Solution:

    def __init__(self, a: list[int]):
        self.original = a.copy()
        self.a = a

    # O(n) time
    def reset(self) -> list[int]:
        self.a = self.original
        self.original = self.original.copy()
        return self.a

    # O(n) time
    def shuffle(self) -> list[int]:
        for i in range(len(self.a) - 1, -1, -1):
            j = random.randint(0, i)
            self.a[i], self.a[j] = self.a[j], self.a[i]
        return self.a


class Test(unittest.TestCase):
    def test(self):
        t = Solution([-6, 10, 184])
        print(t.reset())
        print(t.shuffle())
        print(t.reset())
        print(t.shuffle())
        print(t.reset())
        print(t.shuffle())
        print(t.reset())
        print(t.shuffle())


if __name__ == "__main__":
    unittest.main()
