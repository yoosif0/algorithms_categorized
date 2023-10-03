"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        a = list(s)
        nxt = len(a) - 1
        while nxt >= 0:
            r = nxt
            while r >= 0 and a[r] == " ":
                r -= 1
            l = r
            while True:
                if l == 0:
                    break
                if l >= 1 and a[l - 1] == " ":
                    break
                l -= 1
            nxt = l - 1
            while l < r:
                a[r], a[l] = a[l], a[r]
                l += 1
                r -= 1
        return "".join(a)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc"
        )


if __name__ == "__main__":
    unittest.main()
