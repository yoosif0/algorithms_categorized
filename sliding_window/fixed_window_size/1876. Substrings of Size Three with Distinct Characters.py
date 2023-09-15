"""
#easy

https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/
"""

import unittest


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        char_freq = {}
        if len(s) < 3:
            return ans

        def add_char(index: int):
            char = s[index]
            char_freq[char] = char_freq.get(char, 0) + 1

        def remove_char(index: int):
            char = s[index]
            char_freq[char] = char_freq.get(char, 0) - 1
            if char_freq[char] == 0:
                char_freq.pop(char)

        def add_to_ans_if_applicable():
            nonlocal ans
            if len(char_freq) == 3:
                ans += 1

        # initial window
        for i in range(3):
            add_char(i)
        add_to_ans_if_applicable()

        # slide window
        for i in range(3, len(s)):
            add_char(i)
            remove_char(i - 3)
            add_to_ans_if_applicable()
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.countGoodSubstrings("xyzzaz"), 1)
        self.assertEqual(t.countGoodSubstrings("aababcabc"), 4)
        self.assertEqual(t.countGoodSubstrings("x"), 0)


if __name__ == "__main__":
    unittest.main()
