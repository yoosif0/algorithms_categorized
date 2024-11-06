"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number
2356
              a                       b           c
     d      e          f
 j  k  l    j  k  l   j  k  l
mno mno mno

2
abc
#bounded
#combination

"""
import unittest


m = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, s: str) -> list[str]:
        ans = []

        if len(s) == 0:
            return ans

        def dfs(tmp: str, cs: str):
            if len(tmp) == len(s):
                ans.append(tmp)
                return
            for i in range(0, len(cs)):
                c = cs[i]
                for ch in m[c]:
                    dfs(tmp + ch, cs[i + 1 :])

        dfs("", s)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )
        self.assertEqual(
            obj.letterCombinations("2"),
            ["a", "b", "c"],
        )
        self.assertEqual(
            obj.letterCombinations(""),
            [],
        )


if __name__ == "__main__":
    unittest.main()
