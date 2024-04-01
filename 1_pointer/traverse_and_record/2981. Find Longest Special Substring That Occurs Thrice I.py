"""
https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

it's ok to brute force here since the string is small
"""

import collections
import unittest


class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = collections.Counter()
        bst = -1
        for i in range(len(s)):
            # record substrings as long as all characters are the same. O(n2) time
            r = i
            while r < len(s) and s[r] == s[i]:
                cnt[s[i : r + 1]] += 1
                r += 1
        for k in cnt:
            if cnt[k] >= 3:
                bst = max(bst, len(k))
        return bst


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maximumLength("aaaa"), 2)
        self.assertEqual(t.maximumLength("abcdef"), -1)
        self.assertEqual(t.maximumLength("abcaba"), 1)


if __name__ == "__main__":
    unittest.main()
