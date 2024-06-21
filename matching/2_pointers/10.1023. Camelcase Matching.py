"""
@nested-tags:matching/2_pointers
https://leetcode.com/problems/camelcase-matching
"""

import unittest

"""
ForceFeedBack
     p
FB
 z

ForceBarTest
      p
FB
  z
"""


def pat_in(s: str, pat: str):
    p = 0
    z = 0
    while True:
        # if pattern pointer did not reach the end
        if p == len(s) and z < len(pat):
            return False
        elif z == len(pat):
            # return False if there are still capital letters in s
            while p < len(s):
                if s[p].lower() != s[p]:
                    return False
                p += 1
            return True
        elif s[p] == pat[z]:
            p += 1
            z += 1
        elif s[p].lower() == s[p]:
            p += 1
        else:
            return False


class Solution:
    def camelMatch(self, a: list[str], pat: str) -> list[bool]:
        ans = [True for _ in range(len(a))]
        for i in range(len(a)):
            ans[i] = pat_in(a[i], pat)
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(pat_in("mifeqvzphnrv", "mieqvhnrv"), True)
        self.assertEqual(pat_in("uAxaqlzahfialcezsLfj", "AqlzahalcezsLfj"), True)
        self.assertEqual(pat_in("FooBar", "FB"), True)
        self.assertEqual(pat_in("ForceFeedBack", "FB"), False)
        self.assertEqual(pat_in("FooBarTest", "FB"), False)
        self.assertEqual(pat_in("abcd", "z"), False)
        self.assertEqual(t.camelMatch(["abcd"], "z"), [False])
        self.assertEqual(pat_in("Foo", "F"), True)
        self.assertEqual(pat_in("Counter", "Coo"), False)
        self.assertEqual(pat_in("Control", "Coo"), True)
        self.assertEqual(
            t.camelMatch(
                ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                "FB",
            ),
            [True, False, True, True, False],
        )
        self.assertEqual(
            t.camelMatch(
                ["CompetitiveProgramming", "CounterPick", "ControlPanel"],
                "CooP",
            ),
            [False, False, True],
        )
        self.assertEqual(
            t.camelMatch(
                [
                    "mifeqvzphnrv",
                    "mieqxvrvhnrv",
                    "mhieqovhnryv",
                    "mieqekvhnrpv",
                    "miueqrvfhnrv",
                    "mieqpvhzntrv",
                    "gmimeqvphnrv",
                    "mieqvhqyunrv",
                ],
                "mieqvhnrv",
            ),
            [True, True, True, True, True, True, True, True],
        )
        # self.assertEqual(
        #     t.camelMatch(
        #         [
        #             "aksvbjLiknuTzqon",
        #             "ksvjLimflkpnTzqn",
        #             "mmkasvjLiknTxzqn",
        #             "ksvjLiurknTzzqbn",
        #             "ksvsjLctikgnTzqn",
        #             "knzsvzjLiknTszqn",
        #         ],
        #         "ksvjLiknTzqn",
        #     ),
        #     [True, True],
        # )


if __name__ == "__main__":
    unittest.main()
