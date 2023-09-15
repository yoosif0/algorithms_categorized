"""
not_complete
https://leetcode.com/problems/combination-sum/description/
[2,3,6,7], target = 7
[    0    1   2     3      4       5          6           7
    [[]], [], [],   [],    [],    []         ,[],         []
]
i:0
[    0    1   2     3      4       5          6           7
    [[]], [],[[2]],[[3]],  [],    []       ,[[6]],       [[7]]
]
i:1
continue
i:2
[    0    1   2     3      4         5          6           7
    same same same same [[2,2]]    [[2,3]]      same       same
]
i:3
[    0    1   2     3         4       5     6           7
    same same same same      same  same    [[6],[3,3]]   same 
]
i:4
[    0    1   2     3         4        5            6                         7
    same same same same     same      same     [[6],[3,3],[2,2,2]]       [[7],[2,2,3]]
]
i:5
[    0    1   2     3         4           5                     6                         7
    [[]], [],[[2]],[[3]],  [[2,2]]    [[2,3]]       [[6],[3,3],[2,2,2]]       same
]
if candidate is <  i; forget about it
"""


import unittest


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        dp: list[list[list[int]]] = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for i in range(len(dp)):
            if len(dp[i]) < 1:
                continue
            for candidate in candidates:
                if i + candidate >= len(dp):
                    continue
                if candidate < i:
                    print(i, candidate)
                    continue
                all_arrs: list[list[int]] = [
                    *dp[i + candidate],
                    *[arr + [candidate] for arr in dp[i]],
                ]
                dp[i + candidate] = all_arrs
        # print("\t".join(map(str, dp)))
        print(dp)
        return [[]]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(
        t.combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]]
        # )


if __name__ == "__main__":
    unittest.main()
