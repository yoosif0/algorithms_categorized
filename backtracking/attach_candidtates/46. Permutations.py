"""
https://leetcode.com/problems/permutations/

                                First_node
         1                   2                      3                   4
   2     3     4         1   3     4            1   2    4          1   2    3
 3  4   2 4   2  3

The first node has 4 branches. Each of those 4 have 3 branches, then 2, then 1. That's the first for loop loops through
4 candidates then 3 then 2, etc
#bounded
#combination
"""


import unittest


class Solution:
    def permute(self, a: list[int]) -> list[list[int]]:
        ans = []

        def dfs(tmp: list[int], cs: list[int]):
            if len(tmp) == len(a):
                ans.append(tmp)
                return
            for i in range(len(cs)):
                dfs([*tmp, cs[i]], cs[0:i] + cs[i + 1 :])

        dfs([], a)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        # self.assertEqual(
        #     obj.permute([0, 1]),
        #     [[0, 1], [1, 0]],
        # )
        self.assertEqual(
            obj.permute([1, 2, 3]),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )


if __name__ == "__main__":
    unittest.main()
