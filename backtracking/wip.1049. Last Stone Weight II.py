"""
https://leetcode.com/problems/last-stone-weight-ii
[2,7,4,1,8,1]
    2
7 4 1 8 1
"""

import sys
import unittest


class Solution:
    def lastStoneWeightII(self, cs: list[int]) -> int:
        bst = sys.maxsize

        def dfs(vals, cs: list[int]):
            nonlocal bst
            if len(cs) == 1:
                bst = min(bst, cs[0])
                return
            for i in range(len(cs)):
                for j in range(i + 1, len(cs)):
                    dfs((cs[i], cs[j]), cs[0:i] + cs[i + 1 :])

        dfs(cs)
        return bst


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)


if __name__ == "__main__":
    unittest.main()
