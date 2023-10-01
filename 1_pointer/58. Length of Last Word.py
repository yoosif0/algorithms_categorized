"""
https://leetcode.com/problems/length-of-last-word/
"""

import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while r >= 0 and s[r] == " ":
            r -= 1
        ans = 0
        while r >= 0 and s[r] != " ":
            ans += 1
            r -= 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.lengthOfLastWord("hello world    "), 5)
        self.assertEqual(t.lengthOfLastWord(" "), 0)
        self.assertEqual(t.lengthOfLastWord("a"), 1)


if __name__ == "__main__":
    unittest.main()
