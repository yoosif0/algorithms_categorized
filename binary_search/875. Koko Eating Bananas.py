"""
https://leetcode.com/problems/koko-eating-bananas/
[3, 6, 7, 11], 8
l=1, h=biggest_pile
m=6; for loop to check how many hours are needed there which is 6
6<8 so decrease again. try bfs(1,6) which m=3. for loop to find hours>max
so we need to increase speed. try bfs(3,6). m=4. for loop to get 8 hours = max; return m


[30, 11, 23, 4, 20], 5

"""

import unittest
import math


def get_hours_needed(speed: int, piles: list[int]):
    h = 0
    for pile in piles:
        h += math.ceil(pile / speed)
    return h


class Solution:
    def minEatingSpeed(self, piles: list[int], max_hours: int) -> int:
        biggest_pile = max(piles)
        l = 1
        r = biggest_pile
        while l < r:
            speed = (r + l) // 2
            hours_needed = get_hours_needed(speed, piles)
            if hours_needed > max_hours:
                l = speed + 1
            else:
                r = speed
        return l


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minEatingSpeed([3, 6, 7, 11], 8), 4)
        self.assertEqual(t.minEatingSpeed([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(t.minEatingSpeed([30, 11, 23, 4, 20], 6), 23)
        self.assertEqual(t.minEatingSpeed([312884470], 968709470), 1)


if __name__ == "__main__":
    unittest.main()
