"""
https://leetcode.com/problems/group-anagrams/
we know that 2 words are anagrames if they are the same if sorted
"""

import unittest


class Solution:
    def groupAnagrams(self, a: list[str]) -> list[list[str]]:
        m = {}
        for i in range(len(a)):
            s = a[i].sort()
            if not s in m:
                m[s] = []
            m[s].append(a[i])
        ans = [[] for _ in range(len(m))]
        for i, k in enumerate(m):
            ans[i] = m[k]
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [
                ["eat", "tea", "ate"],
                ["tan", "nat"],
                ["bat"],
            ],
        )


if __name__ == "__main__":
    unittest.main()
