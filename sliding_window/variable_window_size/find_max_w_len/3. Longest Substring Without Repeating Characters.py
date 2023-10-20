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

#store_index
#store_last_index
#unique
The idea here is to store the index of the last incident of a character we saw before to 
make it the "l" for the window when the window is no longer sustainable
"""

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        ch_to_i = {}
        l = 0
        for r in range(len(s)):
            if s[r] in ch_to_i and ch_to_i[s[r]] >= l:
                # shift l right to bypass the problematic character
                l = ch_to_i[s[r]] + 1
            else:
                ans = max(r - l + 1, ans)
            ch_to_i[s[r]] = r
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
