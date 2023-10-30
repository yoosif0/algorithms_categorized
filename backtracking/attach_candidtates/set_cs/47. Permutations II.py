"""
https://leetcode.com/problems/permutations-ii/
1 1 2
                                First_node
       1                   2                  
   1       2               1               
   2         1             1

1 2 3
        1            2       3
    2      3        1  3    1  2
    3      2        3  1    2  1
#set_for_candidates
#bounded
"""


import unittest


class Solution:
    def permuteUnique(self, a: list[int]) -> list[list[int]]:
        ans = []

        def dfs(tmp: list[int], cs: list[int]):
            if len(tmp) == len(a):
                ans.append(tmp)
                return
            used_cs = set()
            for i, num in enumerate(cs):
                if num in used_cs:
                    continue
                used_cs.add(num)
                dfs([*tmp, num], cs[0:i] + cs[i + 1 :])

        dfs([], a)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.permuteUnique([1, 1, 2]), [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        )
        self.assertEqual(
            obj.permuteUnique([1, 2, 3]),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )


if __name__ == "__main__":
    unittest.main()
