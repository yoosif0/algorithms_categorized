"""
https://leetcode.com/problems/valid-anagram
"""

import collections
import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


# class Test(unittest.TestCase):
#     def test(self):
#         obj = Solution()


if __name__ == "__main__":
    unittest.main()
