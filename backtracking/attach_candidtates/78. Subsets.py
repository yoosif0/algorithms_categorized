"""
https://leetcode.com/problems/subsets

                     First Node
    1                        2                           3
s  2  3                    s   3                         s
#bounded
#combination
"""

import unittest


class Solution:
    def subsets(self, a: list[int]) -> list[list[int]]:
        ans = []

        def dfs(tmp: list[int], cs: list[int]):
            ans.append(tmp)
            for i, n in enumerate(cs):
                dfs([*tmp, n], cs[i + 1 :])

        dfs([], a)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.subsets([1, 2, 3]),
            [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]],
        )


if __name__ == "__main__":
    unittest.main()
