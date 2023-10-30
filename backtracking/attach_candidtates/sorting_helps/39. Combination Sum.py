"""
https://leetcode.com/problems/combination-sum/


                            2                  3          6           7
                   2      3        6             6          7
       2         3          6 
  2 

If it's too much you don't need to tackle further numbers since candidates are sorted. remember to sort
#sorting_helps
#unbounded
"""
import unittest


class Solution:
    def combinationSum(self, a: list[int], trg: int) -> list[list[int]]:
        ans = []
        a.sort()

        def dfs(tmp: list[int], cs: list[int], ttl: int):
            if ttl == trg:
                ans.append(tmp)
                return
            for i, c in enumerate(cs):
                if ttl + c > trg:
                    break
                dfs([*tmp, c], cs[i:], ttl + c)

        dfs([], a, 0)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.combinationSum([2, 3, 6, 7], 7),
            [[2, 2, 3], [7]],
        )
        # self.assertEqual(
        #     obj.combinationSum([2, 3, 5], 8),
        #     [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        # )
        # self.assertEqual(
        #     obj.combinationSum([2], 1),
        #     [],
        # )
        # self.assertEqual(
        #     obj.combinationSum([8, 7, 4, 3], 11),
        #     [[3, 4, 4], [3, 8], [4, 7]],
        # )


if __name__ == "__main__":
    unittest.main()
