"""
https://leetcode.com/problems/group-anagrams/description/
we know that 2 words are anagrames if they are the same if sorted
"""

import unittest


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_strs = []
        for word in strs:
            sorted_strs.append((word, "".join(sorted(word))))
        sorted_strs.sort(key=lambda x: x[1])
        ans: list[list[str]] = []
        for i, tup in enumerate(sorted_strs):
            if i >= 1 and sorted_strs[i][1] == sorted_strs[i - 1][1]:
                ans[-1].append(tup[0])
            else:
                ans.append([tup[0]])
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [[2, 2, 3], [7]],
        )


if __name__ == "__main__":
    unittest.main()
