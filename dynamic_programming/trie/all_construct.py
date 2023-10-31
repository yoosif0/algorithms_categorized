"""
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""
import unittest
import functools


class Solution:
    def countConstruct(self, t: str, a: list[str]) -> list[list[str]]:
        @functools.cache
        def rcrs(t: str) -> list[list[str]]:
            ans = []
            if t == "":
                return []
            for i in range(len(a)):
                pre = t[: len(a[i])]
                if pre == a[i]:
                    suf = t[len(a[i]) : :]
                    ans += rcrs(suf)
            return ans

        return rcrs(t)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), 1
        )


if __name__ == "__main__":
    unittest.main()
