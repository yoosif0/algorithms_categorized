"""
@nested-tags:sort_alphabetically
https://leetcode.com/problems/longest-common-prefix/
If the array is sorted alphabetically then you can assume that the first element of the array and the last element of the array will have most different prefixes of all comparisons that could be made between strings in the array. If this is true, you only have to compare these two strings.

"""

import unittest


class Solution:
    def longestCommonPrefix(self, a: list[str]) -> str:
        a.sort()
        ans = a[0][0]
        for i in range(min(len(a[0]), len(a[-1]))):
            if a[0][i] != a[-1][i]:
                return a[-1][0:i]
        return ans[0:i]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(obj.longestCommonPrefix(["awa", "abaa", "azara"]), "a")
        self.assertEqual(obj.longestCommonPrefix(["a", "b"]), "")
        self.assertEqual(obj.longestCommonPrefix(["a"]), "a")


if __name__ == "__main__":
    unittest.main()
