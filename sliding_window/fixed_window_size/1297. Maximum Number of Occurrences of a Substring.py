"""
https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/
"""

import unittest


class Solution:
    def maxFreq(self, s: str, maxLetters: int, k: int, _) -> int:
        ans = 0
        window_char_freq = {}
        substr_freq = {}

        def add_char(i: int):
            char = s[i]
            window_char_freq[char] = window_char_freq.get(char, 0) + 1

        # if substr satisfy condition of max letters, then we need to save the substring in our store
        def log_substr_freq(start_index: int):
            if len(window_char_freq) <= maxLetters:
                nonlocal ans
                substr = s[start_index : start_index + k]
                substr_freq[substr] = substr_freq.get(substr, 0) + 1
                ans = max(ans, substr_freq[substr])

        def remove_char(index: int):
            char = s[index]
            window_char_freq[char] = window_char_freq.get(char, 0) - 1
            if window_char_freq[char] == 0:
                window_char_freq.pop(char)

        # build initial window
        for i in range(k):
            add_char(i)
        log_substr_freq(0)

        # slide window
        for i in range(k, len(s)):
            add_char(i)
            remove_char(i - k)
            log_substr_freq(i - k + 1)

        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxFreq("aababcaab", 2, 3, 4), 2)


if __name__ == "__main__":
    unittest.main()
