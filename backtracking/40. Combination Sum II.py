"""
https://leetcode.com/problems/combination-sum-ii/

                            2                  3          6           7
                       3        6             6          7
                         6 
   
1,1,2,5,6,7,10

                                    1                                                 2             5      6       7  10
    1                2        5             6              7                        5   6          
  2 5 6            5         6            6                                        6 
 5  6


"""

import unittest


class Solution:
    def combinationSum2(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        nums.sort()

        def dfs(temp: list[int], candidates: list[int], total: int):
            if total == target:
                ans.append(temp)
                return
            for i, num in enumerate(candidates):
                if i >= 1 and num == candidates[i - 1]:
                    continue
                if total + num > target:
                    break
                temp_copy = temp.copy()
                temp_copy.append(num)
                dfs(temp_copy, candidates[i + 1 :], total + num)

        dfs([], nums, 0)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.combinationSum2([2, 3, 6, 7], 7),
            [[7]],
        )
        self.assertEqual(
            obj.combinationSum2([2, 3, 5], 8),
            [[3, 5]],
        )
        self.assertEqual(
            obj.combinationSum2([2], 1),
            [],
        )
        self.assertEqual(
            obj.combinationSum2([8, 7, 4, 3], 11),
            [[3, 8], [4, 7]],
        )
        self.assertEqual(
            obj.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8),
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
        )


if __name__ == "__main__":
    unittest.main()
