"""
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""
import unittest
import functools


class Solution:
    def canConstruct(self, target: str, substrs: list[str]) -> bool:
        @functools.cache
        def recursCanConstruct(target: str) -> bool:
            if target == "":
                return True
            for i in range(len(substrs)):
                substr = substrs[i]
                first_part_of_target = target[: len(substr)]
                if first_part_of_target == substr:
                    rem = target[len(substr) : :]
                    if recursCanConstruct(rem):
                        return True
            return False

        return recursCanConstruct(target)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), True
        )


if __name__ == "__main__":
    unittest.main()
