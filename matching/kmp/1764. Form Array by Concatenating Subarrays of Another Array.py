"""
@nested-tags:matching/kmp
https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array
"""

import unittest


def kmp(a: list[int], pat: list[int]) -> int:
    dp = [0 for _ in range(len(a))]
    for i in range(1, len(a)):
        v = dp[i - 1]
        while v and a[i] != a[v]:
            v = dp[v - 1]
        dp[i] = v + (a[i] == a[v])
        if dp[i] == len(pat):
            return i
    return -1


class Solution:
    def canChoose(self, groups: list[list[int]], nums: list[int]) -> bool:
        # j is where we start our kmp nums array
        # we only pass nums[j:] and not nums because the new pattern should match a later part of the array
        j = 0
        for pat in groups:
            if j >= len(nums):
                return False
            # kmp
            a = pat + [1111] + nums[j:]
            i = kmp(a, pat)
            if i == -1:
                return False
            j = i - len(pat)
        return True


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.canChoose([[1, -1, -1], [3, -2, 0]], [1, -1, 0, 1, -1, -1, 3, -2, 0]),
            True,
        )
        self.assertEqual(
            t.canChoose([[10, -2], [1, 2, 3, 4]], [1, 2, 3, 4, 10, -2]),
            False,
        )
        self.assertEqual(
            t.canChoose([[1, 2, 3], [3, 4]], [7, 7, 1, 2, 3, 4, 7, 7]),
            False,
        )


if __name__ == "__main__":
    unittest.main()
