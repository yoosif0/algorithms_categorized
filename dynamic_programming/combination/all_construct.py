"""
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""
import unittest
import functools


class Solution:
    def countConstruct(self, target: str, substrs: list[str]) -> list[list[str]]:
        @functools.cache
        def recursCountConstruct(target: str) -> list[list[str]]:
            ans = []
            if target == "":
                return []
            for i in range(len(substrs)):
                substr = substrs[i]
                first_part_of_target = target[: len(substr)]
                if first_part_of_target == substr:
                    rem = target[len(substr) : :]
                    ans += recursCountConstruct(rem)
            return ans

        return recursCountConstruct(target)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), 1
        )


if __name__ == "__main__":
    unittest.main()
