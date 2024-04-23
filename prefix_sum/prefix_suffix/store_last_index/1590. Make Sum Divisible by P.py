"""
https://leetcode.com/problems/make-sum-divisible-by-p/
"""

from itertools import accumulate
import sys
import unittest


class Solution:
    def minSubarray(self, a: list[int], p: int) -> int:
        mod = [n % p for n in a]
        mod_o = {n: i for i, n in enumerate(mod)}
        mod_sm = list(accumulate(mod, lambda acc, x: (acc + x) % p, initial=0))
        print(mod, mod_sm)
        ans = sys.maxsize
        for i in range(1, len(mod_sm)):
            # [6,3,..,...,..] 9
            # [1,2,3] 3
            if mod_sm[i] == 0:
                ans = min(ans, len(mod) - i)
        # [3, 1, 4, 2], 6
        # [4, 5, 8, 5, 4], 7
        if mod_sm[-1] in mod_o:
            ans = min(ans, 1)
        return -1 if ans == sys.maxsize else ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(t.minSubarray([3, 1, 4, 2], 6), 1)
        # self.assertEqual(t.minSubarray([6, 3, 5, 2], 9), 2)
        # self.assertEqual(t.minSubarray([1, 2, 3], 3), 0)
        # self.assertEqual(t.minSubarray([1000000000, 1000000000, 1000000000], 3), 0)
        # self.assertEqual(t.minSubarray([4, 5, 8, 5, 4], 7), 1)
        self.assertEqual(
            t.minSubarray(
                [26, 19, 11, 14, 18, 4, 7, 1, 30, 23, 19, 8, 10, 6, 26, 3], 26
            ),
            3,
        )

        a = [4, 5, 8, 5, 1]
        mod = [4, 5, 1, 5, 1]
        mod_sm = [0, 4, 2, 3, 1, 2]


if __name__ == "__main__":
    unittest.main()
