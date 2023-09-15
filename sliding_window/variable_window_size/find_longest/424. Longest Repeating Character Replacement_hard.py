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



"""
import unittest


class Solution:
    def characterReplacement(self, s, k):
        ans = 0
        char_freq = {}
        highest_freq = 0
        for i in range(len(s)):
            char = s[i]
            char_freq[char] = char_freq.get(char, 0) + 1
            highest_freq = max(char_freq[char], highest_freq)
            if highest_freq + k > ans:
                ans += 1
            else:
                char_to_remove = s[i - ans]
                char_freq[char_to_remove] = char_freq[char_to_remove] - 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.characterReplacement("ABAB", 2), 4)
        self.assertEqual(t.characterReplacement("AABABBA", 1), 4)


if __name__ == "__main__":
    unittest.main()
