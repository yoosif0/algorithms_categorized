"""
https://leetcode.com/problems/get-equal-substrings-within-budget
"""

import unittest


class Solution:
    def equalSubstring(self, s: str, t: str, k: int) -> int:
        a = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        l = 0
        ans = 0
        w = 0
        for r in range(len(a)):
            w += a[r]
            if w > k:
                w -= a[l]
                l += 1
            else:
                ans = max(ans, r - l + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.equalSubstring("abcd", "bcdf", 3), 3)
        self.assertEqual(t.equalSubstring("abcd", "cdef", 3), 1)
        self.assertEqual(t.equalSubstring("abcd", "acde", 0), 1)
        self.assertEqual(t.equalSubstring("krrgw", "zjxss", 19), 2)


if __name__ == "__main__":
    unittest.main()
