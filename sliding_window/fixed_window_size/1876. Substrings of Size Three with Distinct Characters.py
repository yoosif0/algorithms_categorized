"""
#easy

https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
"""

import unittest


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        w = {}
        if len(s) < 3:
            return ans
        # initial window
        for i in range(3):
            ch = s[i]
            w[ch] = w.get(ch, 0) + 1
        # slide window
        i = 2
        while True:
            if len(w) == 3:
                ans += 1
            i += 1
            if i == len(s):
                break
            # add
            ch = s[i]
            w[ch] = w.get(ch, 0) + 1
            # remove
            ch = s[i - 3]
            w[ch] = w.get(ch, 0) - 1
            if w[ch] == 0:
                w.pop(ch)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.countGoodSubstrings("xyzzaz"), 1)
        self.assertEqual(t.countGoodSubstrings("aababcabc"), 4)
        self.assertEqual(t.countGoodSubstrings("x"), 0)


if __name__ == "__main__":
    unittest.main()
