"""
https://leetcode.com/problems/palindrome-partitioning/

example:aab
                        a           
                      s a bN      
                        s

                        
asafjaa



"""


import unittest


def even_palindrome_length(word: str, center: int):
    ans = 2
    for j in range(1, min(len(word) - center - 1, center + 1)):
        if word[center - j] == word[center + j + 1]:
            ans += 2
        else:
            break
    return ans


def odd_palindrome_length(word: str, center: int):
    ans = 1
    for j in range(1, min(len(word) - center, center + 1)):
        if word[center - j] == word[center + j]:
            ans += 2
        else:
            break
    return ans


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def dfs(tmp: list[int], cs: list[int]):
            if len(tmp) == len(nums):
                ans.append(tmp)
                return
            for i, num in enumerate(cs):
                dfs([*tmp, num], cs[0:i] + cs[i + 1 :])

        dfs([], nums)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(odd_palindrome_length("aba", 1), 3)
        self.assertEqual(odd_palindrome_length("aabaa", 2), 5)
        self.assertEqual(even_palindrome_length("aa", 0), 2)
        self.assertEqual(even_palindrome_length("baab", 1), 4)
        self.assertEqual(even_palindrome_length("cbaabc", 2), 6)
        self.assertEqual(even_palindrome_length("cbaabd", 2), 4)
        self.assertEqual(even_palindrome_length("cbaab", 2), 4)


if __name__ == "__main__":
    unittest.main()
