"""
https://leetcode.com/problems/find-all-anagrams-in-a-string
#reach_0_state
#unroll
We unroll a hashmap untill it reach 0 keys
"""
import unittest


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        k = len(p)
        if k > len(s):
            return []
        w = {}
        # add char freq by negative for p, whenever the window sees the same character, we increment the val.
        # whenever we reach 0 and the window has no keys, we know we have an answer
        for i in range(len(p)):
            ch = p[i]
            w[ch] = w.get(ch, 0) - 1
        # initial window
        for i in range(k):
            ch = s[i]
            w[ch] = w.get(ch, 0) + 1
            if w[ch] == 0:
                w.pop(ch)
        ans = []
        i = k - 1
        while True:
            if len(w) == 0:
                ans.append(i - k + 1)
            i += 1
            if i >= len(s):
                break
            # add new ch
            ch = s[i]
            w[ch] = w.get(ch, 0) + 1
            if w[ch] == 0:
                w.pop(ch)
            # remove old ch
            ch = s[i - k]
            w[ch] = w.get(ch, 0) - 1
            if w[ch] == 0:
                w.pop(ch)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.findAnagrams("cbaebabacd", "abc"),
            [0, 6],
        )
        self.assertEqual(
            t.findAnagrams("abab", "ab"),
            [0, 1, 2],
        )


if __name__ == "__main__":
    unittest.main()
