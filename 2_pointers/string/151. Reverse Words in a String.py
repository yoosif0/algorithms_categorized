"""
https://leetcode.com/problems/reverse-words-in-a-string/
"""
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        # untrim
        a = s.split(" ")
        for i in range(len(a)):
            if a[i] != "":
                ans.append(a[i])

        # switch words using 2 pointers
        l = 0
        r = len(ans) - 1
        while l < r:
            ans[l], ans[r] = ans[r], ans[l]
            l += 1
            r -= 1
        return " ".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(t.reverseWords("the sky is blue"), "blue is sky the")
        # self.assertEqual(t.reverseWords("   hello world   "), "world hello")
        # self.assertEqual(t.reverseWords(" a  good      example   "), "example good a")


if __name__ == "__main__":
    unittest.main()
