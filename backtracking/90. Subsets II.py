"""
https://leetcode.com/problems/subsets-ii/


         1                2                
s          2             s   2
         s  2                 s
            s
"""
import unittest


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        nums.sort()

        def dfs(temp: list[int], candidates: list[int]):
            for i, num in enumerate(candidates):
                if i >= 1 and num == candidates[i - 1]:
                    continue
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
            obj.subsetsWithDup([1, 2, 2]),
            [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
        )


if __name__ == "__main__":
    unittest.main()
