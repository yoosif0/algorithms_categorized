"""
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""
import unittest
import functools


class Solution:
    def canConstruct(self, t: str, a: list[str]) -> bool:
        @functools.cache
        def rcrs(t: str) -> bool:
            if t == "":
                return True
            for i in range(len(a)):
                pre = t[: len(a[i])]
                if pre == a[i]:
                    suf = t[len(a[i]) : :]
                    if rcrs(suf):
                        return True
            return False

        return rcrs(t)


"""
abcdef
111111
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), True
        )


if __name__ == "__main__":
    unittest.main()
