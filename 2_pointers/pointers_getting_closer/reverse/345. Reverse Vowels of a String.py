"""
https://leetcode.com/problems/reverse-vowels-of-a-string/
#nested_while
"""
import unittest


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1
        vwl = set({"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"})
        while l < r:
            while s[l] not in vwl and l < r:
                l += 1
            while s[r] not in vwl and l < r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.reverseVowels("hello"), "holle")


if __name__ == "__main__":
    unittest.main()
