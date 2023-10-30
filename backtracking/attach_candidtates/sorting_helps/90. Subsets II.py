"""
https://leetcode.com/problems/subsets-ii/


         1                2                
s          2             s   2
         s  2                 s
            s
#bounded
"""
import unittest


class Solution:
    def subsetsWithDup(self, a: list[int]) -> list[list[int]]:
        ans = []
        a.sort()

        def dfs(tmp: list[int], cs: list[int]):
            ans.append(tmp)
            for i, n in enumerate(cs):
                if i >= 1 and n == cs[i - 1]:
                    continue
                dfs([*tmp, n], cs[i + 1 :])

        dfs([], a)
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
