"""
@nested-tags:matching/brute_force,cmp
https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i
2 <= n == nums.length <= 100

like version 2 but with smaller inputs (brute force works and no need for kmp)
"""

import unittest


def cmp(a, b):
    return (a > b) - (a < b)


class Solution:
    def countMatchingSubarrays(self, a: list[int], pat: list[int]) -> int:
        # convert a to change_arr to have the same format as pattern (pat)
        a = [cmp(a[i + 1], a[i]) for i in range(len(a) - 1)]
        pat = tuple(pat)
        ans = 0
        for i in range(len(a) - len(pat) + 1):
            if pat == tuple(a[i : i + len(pat)]):
                ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.countMatchingSubarrays([1, 2, 3, 4, 5, 6], [1, 1]),
            4,
        )
        self.assertEqual(
            t.countMatchingSubarrays([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1]),
            2,
        )
        self.assertEqual(
            t.countMatchingSubarrays([481251768, 481251768, 481251768, 463564806], [0]),
            2,
        )


if __name__ == "__main__":
    unittest.main()
