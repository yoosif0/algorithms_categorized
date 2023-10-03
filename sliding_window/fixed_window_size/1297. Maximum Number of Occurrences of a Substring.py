"""
https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
"""

import unittest


class Solution:
    def maxFreq(self, s: str, maxLetters: int, k: int, _) -> int:
        ans = 0
        w = {}
        substr_freq = {}
        # initial window
        for i in range(k):
            ch = s[i]
            w[ch] = w.get(ch, 0) + 1
        # slide window
        i = k - 1
        while True:
            # if substr satisfy condition of max letters, then we need to save the substring in our store
            if len(w) <= maxLetters:
                substr = s[i - k + 1 : i + 1]
                substr_freq[substr] = substr_freq.get(substr, 0) + 1
                ans = max(ans, substr_freq[substr])
            i += 1
            if i == len(s):
                break
            # add
            ch = s[i]
            w[ch] = w.get(ch, 0) + 1
            # remove
            ch = s[i - k]
            w[ch] -= 1
            if w[ch] == 0:
                w.pop(ch)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxFreq("aababcaab", 2, 3, 4), 2)


if __name__ == "__main__":
    unittest.main()
