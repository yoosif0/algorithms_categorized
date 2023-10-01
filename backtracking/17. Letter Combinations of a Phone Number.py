"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number
2356
              a                                b                   c
     d      e          f
 j  k  l    j  k  l   j  k  l
mno mno mno

2
abc

"""
import unittest


letters = {
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
    def letterCombinations(self, digits: str) -> list[str]:
        ans = []

        if len(digits) == 0:
            return ans

        def dfs(tmp: str, cs: str):
            if len(tmp) == len(digits):
                ans.append(tmp)
                return
            for i in range(0, len(cs)):
                c = cs[i]
                for letter in letters[c]:
                    dfs(tmp + letter, cs[i + 1 :])

        dfs("", digits)
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
