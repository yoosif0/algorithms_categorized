"""
https://leetcode.com/problems/koko-eating-bananas/
[3, 6, 7, 11], 8
The trick here is to know that the limits are 1 and max(a) for lo and hi respctively

"""

import unittest


class Solution:
    def minEatingSpeed(self, a: list[int], t: int) -> int:
        l = 1
        r = max(a)
        while l < r:
            m = (r + l) // 2
            # (n - 1) // m + 1 is faster than math.ceil
            hrs = sum((n - 1) // m + 1 for n in a)
            feasible = hrs <= t
            if not feasible:
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
