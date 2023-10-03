"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"ABBBBBBBAAA"
ABB
"""
import unittest


class Solution:
    def winnerOfGame(self, s: str) -> bool:
        a_count = 0
        b_count = 0
        all_a = "AAA"
        all_b = "BBB"
        for i in range(len(s) - 2):
            window = s[i : i + 3]
            if window == all_a:
                a_count += 1
            elif window == all_b:
                b_count += 1
        return a_count > b_count


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.winnerOfGame("AAABABB"), True)
        self.assertEqual(t.winnerOfGame("AA"), False)
        self.assertEqual(t.winnerOfGame("ABBBBBBBAAA"), False)
        self.assertEqual(t.winnerOfGame("AAAABBBB"), False)


if __name__ == "__main__":
    unittest.main()
