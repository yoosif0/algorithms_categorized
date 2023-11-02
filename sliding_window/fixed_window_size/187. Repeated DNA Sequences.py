"""
https://leetcode.com/problems/repeated-dna-sequences
#once_twice
"""
import unittest


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) <= 10:
            return []
        k = 10
        w = 0
        once = set()
        twice = set()
        # Slide window
        while True:
            cur = s[w : w + k]
            if cur in once:
                twice.add(cur)
            else:
                once.add(cur)
            if w + k == len(s):
                break
            w += 1
        return list(twice)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(
        #     t.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"),
        #     ["CCCCCAAAAA", "AAAAACCCCC"],
        # )
        self.assertEqual(
            t.findRepeatedDnaSequences("A"),
            [],
        )


if __name__ == "__main__":
    unittest.main()
