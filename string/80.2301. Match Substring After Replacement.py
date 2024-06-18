"""
@nested-tags:string/matching,not_solved
https://leetcode.com/problems/match-substring-after-replacement
"""

import unittest
from collections import deque


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: list[list[str]]) -> bool:
        sub = list(sub)
        m = {}
        for i in range(len(sub)):
            ch = sub[i]
            if ch not in m:
                m[ch] = deque([])
            m[ch].append(i)
        for x in mappings:
            if x[0] not in m or not m[x[0]]:
                continue
            i = m[x[0]].popleft()
            sub[i] = x[1]

        sub = "".join(sub)
        for i in range(len(s) - len(sub)):
            if s[i : i + len(sub)] == sub:
                return True
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
        # self.assertEqual(
        #     t.matchReplacement(
        #         "Fool33tbaR",
        #         "leetd",
        #         [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]],
        #     ),
        #     True,
        # )


if __name__ == "__main__":
    unittest.main()
