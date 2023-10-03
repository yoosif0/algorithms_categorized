"""
https://leetcode.com/problems/longest-repeating-character-replacement/




AABABDACAAAAA


A 1
A 2
B 3
A 4
B 4; 
D 4;
A 4
C 4 
A 4 
A l=6
A do nothing update max
A do nothing

AABABBA 1
A
AA
AAB
AABA 4
AABAB not work
ABAB not work
BAB  work
BABB  work
BABBA  not work
ABBA  not work
BBA work


#no_need_nested_while
#no_need_track_l
"""
import unittest


class Solution:
    def characterReplacement(self, s, k):
        ans = 0
        ch_freq = {}
        highest_freq = 0
        for r in range(len(s)):
            ch = s[r]
            ch_freq[ch] = ch_freq.get(ch, 0) + 1
            highest_freq = max(ch_freq[ch], highest_freq)
            if highest_freq + k > ans:
                ans += 1
            else:
                # remove
                ch = s[r - ans]
                ch_freq[ch] = ch_freq[ch] - 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.characterReplacement("ABAB", 2), 4)
        self.assertEqual(t.characterReplacement("AABABBA", 1), 4)


if __name__ == "__main__":
    unittest.main()
