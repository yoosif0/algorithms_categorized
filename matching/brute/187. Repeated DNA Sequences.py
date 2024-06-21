"""
@nested-tags:matching/brute_force,seen_twice,sliding_w
https://leetcode.com/problems/repeated-dna-sequences
it's ok to keep slicing the string into substrings (brute force) since substring length is small (10)
"""

import unittest


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        k = 10
        seen = set()
        twice = set()
        for i in range(len(s) - k):
            cur = s[i : i + k]
            if cur in seen:
                twice.add(cur)
            else:
                seen.add(cur)
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
