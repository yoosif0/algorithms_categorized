"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"ABBBBBBBAAA"
ABB
"""
import unittest


class Solution:
    def winnerOfGame(self, s: str) -> bool:
        a_cnt = 0
        b_cnt = 0
        all_a = "AAA"
        all_b = "BBB"
        for i in range(len(s) - 2):
            w = s[i : i + 3]
            if w == all_a:
                a_cnt += 1
            elif w == all_b:
                b_cnt += 1
        return a_cnt > b_cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.winnerOfGame("AAABABB"), True)
        self.assertEqual(t.winnerOfGame("AA"), False)
        self.assertEqual(t.winnerOfGame("ABBBBBBBAAA"), False)
        self.assertEqual(t.winnerOfGame("AAAABBBB"), False)


if __name__ == "__main__":
    unittest.main()
