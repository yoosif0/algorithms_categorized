"""
https://leetcode.com/problems/reverse-string-ii/
"""
import unittest


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        fl = True
        ans = []
        a = []
        for i in range(len(s)):
            a.append(s[i])
            if len(a) == k or i == len(s) - 1:
                ans.append("".join(a[::-1] if fl else a))
                fl = not fl
                a = []
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.reverseStr("onetwoten", 3), "enotwonet")
        self.assertEqual(t.reverseStr("abcdefg", 2), "bacdfeg")


if __name__ == "__main__":
    unittest.main()
