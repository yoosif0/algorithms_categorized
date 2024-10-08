"""
@nested-tags:matching/kmp,cmp
https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

This is like version 1 of the question but with higher inputs. Version can be brute forced

2 <= n == nums.length <= 10^6
"""

import unittest


def cmp(a, b):
    return (a > b) - (a < b)


class Solution:
    def countMatchingSubarrays(self, a: list[int], pat: list[int]) -> int:
        # convert a to change_arr to have the same format as pattern (pat)
        a = [cmp(a[i + 1], a[i]) for i in range(len(a) - 1)]
        # kmp
        a = pat + [-2] + a
        dp = [0 for _ in range(len(a))]
        ans = 0
        j = 0
        i = 1
        while i < len(a):
            if a[i] == a[j]:
                dp[i] = j + 1
                if dp[i] == len(pat):
                    ans += 1
                i += 1
                j += 1
            elif j != 0:
                j = dp[j - 1]
            else:
                dp[i] = 0
                i += 1
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
