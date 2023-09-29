"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/
"""
import unittest


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_arr = list(s)
        l = 0
        r = len(s) - 1
        vowels = set({"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"})
        while l < r:
            while s_arr[l] not in vowels and l < r:
                l += 1
            while s_arr[r] not in vowels and l < r:
                r -= 1
            s_arr[l], s_arr[r] = s_arr[r], s_arr[l]
            l += 1
            r -= 1
        return "".join(s_arr)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.reverseVowels("hello"), "holle")


if __name__ == "__main__":
    unittest.main()
