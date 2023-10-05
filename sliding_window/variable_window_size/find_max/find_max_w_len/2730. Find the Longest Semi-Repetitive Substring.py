"""
https://leetcode.com/problems/find-the-longest-semi-repetitive-substring
002020
54001010223691098234
5400101022 cant so I store the index of repitive part and put l at it

They want the length of the longest substring where maximum one consecutive val exists.
I keep moving window trying to maximize and store the index of consecutive val. Whenever, I meet
another consecutive val, I update w state and shift l.
#store_index
"""

import unittest


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 1
        l = 0
        # the state of the window is the index of consecutive val if exists
        w = None
        for r in range(1, len(s)):
            if s[r] == s[r - 1] and w:
                l = w
                w = r
            else:
                if s[r] == s[r - 1] and not w:
                    w = r
                ans = max(ans, r - l + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.longestSemiRepetitiveSubstring("52233"), 4)
        self.assertEqual(t.longestSemiRepetitiveSubstring("5494"), 4)
        self.assertEqual(t.longestSemiRepetitiveSubstring("0001"), 3)
        self.assertEqual(t.longestSemiRepetitiveSubstring("0010"), 4)
        self.assertEqual(t.longestSemiRepetitiveSubstring("1111111"), 2)


if __name__ == "__main__":
    unittest.main()
