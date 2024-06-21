"""
@nested-tags:matching/kmp,binary_search/remove_from_both
https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i
"""

import unittest


def kmp(s: str, pat: str) -> list[int]:
    s = pat + "__" + s
    ans = []
    dp = [0 for _ in range(len(s))]
    j = 0
    i = 1
    while i < len(s):
        if s[i] == s[j]:
            dp[i] = j + 1
            if dp[i] == len(pat):
                ans.append(i - 2 * len(pat) - 1)
            i += 1
            j += 1
        elif j != 0:
            j = dp[j - 1]
        else:
            dp[i] = 0
            i += 1
    return ans


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        # find all occurrences of a and b patterns in s
        # a and b are the indecis of for all occurrences of a and b respecitively in s
        a = kmp(s, a)
        b = kmp(s, b)
        # for each ai, there should exist a bi that ai-15 <= bi <= ai+15
        ans = []
        for ai in a:
            l = 0
            r = len(b) - 1
            while l <= r:
                mid = (l + r) // 2
                # bi can't be greater than ai
                if b[mid] - ai > k:
                    r = mid - 1
                # bi can't be so much smaller than ai
                elif ai - b[mid] > k:
                    l = mid + 1
                else:
                    ans.append(ai)
                    break
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.beautifulIndices(
                "isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15
            ),
            [16, 33],
        )
        self.assertEqual(
            t.beautifulIndices("abcd", "a", "a", 4),
            [0],
        )
        self.assertEqual(
            t.beautifulIndices("bavgoc", "ba", "c", 6),
            [0],
        )


if __name__ == "__main__":
    unittest.main()
