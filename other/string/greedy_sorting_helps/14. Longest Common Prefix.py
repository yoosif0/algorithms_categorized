"""
https://leetcode.com/problems/longest-common-prefix/description/
If the array is sorted alphabetically then you can assume that the first element of the array and the last element of the array will have most different prefixes of all comparisons that could be made between strings in the array. If this is true, you only have to compare these two strings.

"""
import unittest


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[len(strs) - 1]
        common = 0
        while common < len(first) and first[0 : common + 1] == last[0 : common + 1]:
            common += 1
        return first[0:common]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(obj.longestCommonPrefix(["awa", "abaa", "azara"]), "a")
        self.assertEqual(obj.longestCommonPrefix(["a", "b"]), "")
        self.assertEqual(obj.longestCommonPrefix(["a"]), "a")


if __name__ == "__main__":
    unittest.main()
