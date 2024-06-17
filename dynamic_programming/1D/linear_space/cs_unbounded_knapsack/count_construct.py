"""
@nested-tags:knapsack/unbounded
https://www.youtube.com/watch?v=oBt53YbR9Kk
#count_combinations
"""

import unittest
import functools


class Solution:
    def countConstruct(self, s: str, cs: list[str]) -> int:
        cnt = 0

        @functools.cache
        def rcrs(s: str) -> int:
            nonlocal cnt

            for c in cs:
                if s[: len(c)] == c:
                    suf = s[len(c) : :]
                    # we're updating solution here because the rcrs fn is cached and would lead to bad results
                    if suf == "":
                        cnt += 1
                        return
                    rcrs(suf)

        rcrs(s)
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), 1
        )
        self.assertEqual(
            t.countConstruct("abcdef", ["ab", "abc", "cd", "def", "ef", "abcd"]), 2
        )


if __name__ == "__main__":
    unittest.main()
