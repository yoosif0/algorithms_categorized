"""
https://leetcode.com/problems/longest-repeating-character-replacement/
#no_need_valid_w
#find_max_w_len
"""

import collections
import unittest


class Solution:
    def characterReplacement(self, s, k):
        m = collections.Counter()
        # mx cnt in w
        mx = 0
        l = 0
        ans = 0
        for r in range(len(s)):
            m[s[r]] += 1
            mx = max(mx, m[s[r]])
            if r - l + 1 - mx > k:
                m[s[l]] -= 1
                l += 1
            else:
                ans = max(ans, r - l + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.characterReplacement("ABAB", 2), 4)
        self.assertEqual(t.characterReplacement("AABABBA", 1), 4)


if __name__ == "__main__":
    unittest.main()
