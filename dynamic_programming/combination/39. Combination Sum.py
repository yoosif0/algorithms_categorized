"""
not_complete
https://leetcode.com/problems/combination-sum/
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
    def combinationSum(self, cs: list[int], target: int) -> list[list[int]]:
        dp: list[list[list[int]]] = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for i in range(len(dp)):
            if len(dp[i]) < 1:
                continue
            for c in cs:
                if i + c >= len(dp):
                    continue
                if c < i:
                    print(i, c)
                    continue
                all_arrs: list[list[int]] = [
                    *dp[i + c],
                    *[arr + [c] for arr in dp[i]],
                ]
                dp[i + c] = all_arrs
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
