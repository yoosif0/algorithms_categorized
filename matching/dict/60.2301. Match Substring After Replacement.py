"""
@nested-tags:matching/dict/set,matching/double_traversal
https://leetcode.com/problems/match-substring-after-replacement
"""

import unittest


class Solution:
    def matchReplacement(self, s: str, s2: str, mappings: list[list[str]]) -> bool:
        m = {}
        for x in mappings:
            if x[0] not in m:
                m[x[0]] = set()
            m[x[0]].add(x[1])

        for i in range(len(s) - len(s2) + 1):
            for j in range(len(s2) + 1):
                if j == len(s2):
                    return True
                elif s[i + j] == s2[j]:
                    continue
                elif s2[j] in m and s[i + j] in m[s2[j]]:
                    continue
                else:
                    break
        return False


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.matchReplacement(
                "fool3e7bar", "leet", [["e", "3"], ["t", "7"], ["t", "8"]]
            ),
            True,
        )
        self.assertEqual(
            t.matchReplacement("fooleetbar", "f00l", [["o", "0"]]),
            False,
        )
        self.assertEqual(
            t.matchReplacement(
                "Fool33tbaR",
                "leetd",
                [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]],
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
