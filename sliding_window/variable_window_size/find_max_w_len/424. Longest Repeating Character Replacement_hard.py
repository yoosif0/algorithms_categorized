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


#no_need_valid_w
#find_max_w_len
"""
from dataclasses import dataclass
from typing import Dict
import unittest

"""
ABBABDBCAAAAA   4
A 1
B 2 k 3
B 3 k=3 main_ch = B
A 4 k=2
B 5 
D 6 k=1
B 7
C 8 k=0
A can't

  can't. try to make main char different. check the most frequent char and assume it's B. 
    k=freq[B]-freq[l]. if k is still ==0, then I need to shift l  

"""


class Window:
    def __init__(self, k: int):
        self.ch_frq = {}
        self.balance = k
        self.k = k

    def update_metadata(self):
        max_count = 0
        total_count = 0
        for _, v in self.ch_frq.items():
            total_count += v
            if v >= max_count:
                max_count = v
        self.balance = self.k - (total_count - max_count)

    def add(self, ch: str):
        self.ch_frq[ch] = self.ch_frq.get(ch, 0) + 1
        self.update_metadata()

    def remove(self, ch: str):
        self.ch_frq[ch] -= 1
        self.update_metadata()


class Solution:
    def characterReplacement(self, s, k):
        w = Window(k)
        w.add(s[0])
        l = 0
        ans = 1
        for r in range(1, len(s)):
            w.add(s[r])
            if w.balance < 0:
                w.remove(s[l])
                l += 1
            else:
                ans = max(ans, r - l + 1)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.characterReplacement("ABAB", 2), 4)
        self.assertEqual(t.characterReplacement("AABABBA", 1), 4)


if __name__ == "__main__":
    unittest.main()
