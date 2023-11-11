"""
https://leetcode.com/problems/reverse-string-ii/
"""
import unittest


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        i = 0
        while True:
            if i >= len(s):
                break
            ans.append(s[i : i + k][::-1])
            if i + k >= len(s):
                break
            ans.append(s[i + k : i + 2 * k])
            i += 2 * k
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.reverseStr("onetwoten", 3), "enotwonet")
        self.assertEqual(t.reverseStr("abcdefg", 2), "bacdfeg")


if __name__ == "__main__":
    unittest.main()
