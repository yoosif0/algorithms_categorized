"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
a 1 {a:0}
b 2 {a:0, b:1}
c 3 {a:0, b:1, c:2}
a window:"bca". current_max=window_length  3-0
d 4
c reset window to "adc". m[c]==2
j 4
b
z
d
a 4
"""

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        char_to_index = {}
        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in char_to_index and char_to_index[char] >= l:
                # shift start of window to the right to bypass the problematic character
                l = char_to_index[char] + 1
            char_to_index[char] = r
            window_length = r - l + 1
            ans = max(window_length, ans)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.lengthOfLongestSubstring("abc"), 3)
        self.assertEqual(t.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(t.lengthOfLongestSubstring("abcabcbbzdafjl"), 7)
        self.assertEqual(t.lengthOfLongestSubstring("bbbbbb"), 1)
        self.assertEqual(t.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
