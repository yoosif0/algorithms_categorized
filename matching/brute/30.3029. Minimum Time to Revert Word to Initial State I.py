"""
@nested-tags:matching/brute_force
https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i

aba_caba
    0123      needs one extra

aba_dcaba
    00123      needs 2 extra

abadcaba

"""

import unittest


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        i = 1
        while True:
            suf = word[i * k :]
            pre = word[: len(suf)]
            if suf == pre:
                return i
            i += 1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.minimumTimeToInitialState("abacaba", 3), 2)
        self.assertEqual(t.minimumTimeToInitialState("abacaba", 4), 1)
        self.assertEqual(t.minimumTimeToInitialState("abcbabcd", 2), 4)
        self.assertEqual(t.minimumTimeToInitialState("ba", 1), 2)


if __name__ == "__main__":
    unittest.main()
