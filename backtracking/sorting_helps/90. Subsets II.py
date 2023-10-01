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
        ans = []
        nums.sort()

        def dfs(tmp: list[int], cs: list[int]):
            ans.append(tmp)
            for i, num in enumerate(cs):
                if i >= 1 and num == cs[i - 1]:
                    continue
                dfs([*tmp, num], cs[i + 1 :])

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
