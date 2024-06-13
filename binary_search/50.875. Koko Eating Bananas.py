"""
@nested-tags:binary_search/no_arr/consumption,binary_search/remove_from_l
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
            mid = (r + l) // 2
            # (n - 1) // mid + 1 is faster than math.ceil
            hrs = sum((n - 1) // mid + 1 for n in a)
            if hrs <= t:
                l = mid + 1
            else:
                r = mid
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
