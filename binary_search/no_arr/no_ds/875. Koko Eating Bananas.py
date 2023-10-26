"""
https://leetcode.com/problems/koko-eating-bananas/
[3, 6, 7, 11], 8
l=1, h=biggest_pile
m=6; for loop to check how many hours are needed there which is 6
6<8 so decrease again. try bfs(1,6) which m=3. for loop to find hours>max
so we need to increase speed. try bfs(3,6). m=4. for loop to get 8 hours = max; return m
"""

import unittest
import math


class Solution:
    def minEatingSpeed(self, a: list[int], t: int) -> int:
        l = 1
        r = max(a)
        while l < r:
            m = (r + l) // 2
            mv = 0
            for i in range(len(a)):
                mv += math.ceil(a[i] / m)
            if mv > t:
                l = m + 1
            else:
                r = m
        return l


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minEatingSpeed([3, 6, 7, 11], 8), 4)
        self.assertEqual(t.minEatingSpeed([4, 11, 20, 23, 30], 5), 30)
        self.assertEqual(t.minEatingSpeed([4, 11, 20, 23, 30], 6), 23)
        self.assertEqual(t.minEatingSpeed([312884470], 968709470), 1)


"""
4, 11, 20, 23, 30  5
4  15  35  58  88
"""

if __name__ == "__main__":
    unittest.main()
