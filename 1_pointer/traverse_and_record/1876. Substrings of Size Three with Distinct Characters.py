"""
#easy
#counting_sliding_window

You don't need sliding window technique since the window size is very small (3)

https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
"""

import unittest


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s) - 2):
            if len(set(s[i : i + 3])) == 3:
                cnt += 1
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.countGoodSubstrings("xyzzaz"), 1)
        self.assertEqual(t.countGoodSubstrings("aababcabc"), 4)
        self.assertEqual(t.countGoodSubstrings("x"), 0)


if __name__ == "__main__":
    unittest.main()
