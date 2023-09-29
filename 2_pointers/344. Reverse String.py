"""
https://leetcode.com/problems/reverse-string/
"""
import unittest


class Solution:
    def reverseString(self, s: list[str]) -> None:
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        t.reverseString(["h", "e", "l", "l", "o"])


if __name__ == "__main__":
    unittest.main()
