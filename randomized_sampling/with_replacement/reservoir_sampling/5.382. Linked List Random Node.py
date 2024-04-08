"""
https://leetcode.com/problems/linked-list-random-node
"""

import random
from typing import Optional
import unittest
from algoutils.list_node import ListNode, ll


class Solution:
    def __init__(self, p: Optional[ListNode]):
        self.a = []
        while p:
            self.a.append(p)
            p = p.next

    def getRandom(self) -> int:
        return random.choice(self.a).val


class Test(unittest.TestCase):
    def test(self):
        t = Solution(ll([1, 2, 3]))
        print(t.getRandom())
        print(t.getRandom())
        print(t.getRandom())
        print(t.getRandom())
        print(t.getRandom())
        print(t.getRandom())
        print(t.getRandom())
        print(t.getRandom())
        print(t.getRandom())


if __name__ == "__main__":
    unittest.main()
