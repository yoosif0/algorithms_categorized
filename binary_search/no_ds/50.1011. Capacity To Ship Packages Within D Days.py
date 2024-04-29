"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
The trick here is to know that the limits are max(a) and sum(a) for lo and hi respctively
"""

import unittest


class Solution:
    def shipWithinDays(self, a: list[int], k: int) -> int:
        def feasible(m: int):
            k2 = 1
            cur = 0
            for i in range(len(a)):
                cur += a[i]
                if cur > m:
                    cur = a[i]
                    k2 += 1
                elif cur == m:
                    cur = 0
                    k2 += 1
            if cur == 0:
                k2 -= 1
            return k2 <= k

        l = max(a)
        r = sum(a)
        while l < r:
            m = (l + r) // 2
            if not feasible(m):
                l = m + 1
            else:
                r = m
        return l


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)
        self.assertEqual(t.shipWithinDays([3, 2, 2, 4, 1, 4], 3), 6)
        self.assertEqual(t.shipWithinDays([1, 2, 3, 1, 1], 4), 3)


if __name__ == "__main__":
    unittest.main()
