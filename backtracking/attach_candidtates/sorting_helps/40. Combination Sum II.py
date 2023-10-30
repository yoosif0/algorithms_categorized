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

#sorting_helps
#bounded
"""

import unittest


class Solution:
    def combinationSum2(self, a: list[int], trg: int) -> list[list[int]]:
        ans = []
        a.sort()

        def dfs(tmp: list[int], cs: list[int], ttl: int):
            if ttl == trg:
                ans.append(tmp)
                return
            for i, n in enumerate(cs):
                if i >= 1 and n == cs[i - 1]:
                    continue
                if ttl + n > trg:
                    break
                dfs([*tmp, n], cs[i + 1 :], ttl + n)

        dfs([], a, 0)
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
