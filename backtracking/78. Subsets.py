"""
https://leetcode.com/problems/subsets

                     First Node
    1                        2                           3
s  2  3                    s   3                         s
"""

import unittest


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]

        def dfs(temp: list[int], candidates: list[int]):
            for i, num in enumerate(candidates):
                cur_copy = temp.copy()
                cur_copy.append(num)
                ans.append(cur_copy)
                candidates_copy = candidates[i + 1 :]
                dfs(cur_copy, candidates_copy)

        dfs([], nums)
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
