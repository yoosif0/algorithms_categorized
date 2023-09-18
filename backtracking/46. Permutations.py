"""
https://leetcode.com/problems/permutations/

                                First_node
         1                   2                      3                   4
   2     3     4         1   3     4            1   2    4          1   2    3
 3  4   2 4   2  3

The first node has 4 branches. Each of those 4 have 3 branches, then 2, then 1. That's the first for loop loops through
4 candidates then 3 then 2, etc

"""


import unittest


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def dfs(temp: list[int], candidates: list[int]):
            if len(temp) == len(nums):
                ans.append(temp)
                return
            for num in candidates:
                temp_copy = temp.copy()
                temp_copy.append(num)
                candidates_copy = candidates.copy()
                # not a big deal since we are O(n) anyways inside this loop and the "candidates" are not too much. Even if candidates are too much the main culprit is the exponenetial time it takes from backtracking
                candidates_copy.remove(num)
                dfs(temp_copy, candidates_copy)

        dfs([], nums)
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
