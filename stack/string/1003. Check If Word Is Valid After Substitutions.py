"""
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
"""
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch != "c":
                st.append(ch)
            elif len(st) >= 2 and st[-2] == "a" and st[-1] == "b":
                st.pop()
                st.pop()
            else:
                return False
        return len(st) == 0


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isValid("aabcbc"), True)
        self.assertEqual(obj.isValid("abcabcababcc"), True)
        self.assertEqual(obj.isValid("abccba"), False)


if __name__ == "__main__":
    unittest.main()
