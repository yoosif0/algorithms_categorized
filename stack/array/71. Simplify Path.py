"""
https://leetcode.com/problems/simplify-path/
#string
"""

import unittest


class Solution:
    def simplifyPath(self, s: str) -> str:
        st = []
        for ch in s.split("/"):
            if len(ch) == 0:
                continue
            if ch not in ("..", "."):
                st.append(ch)
            elif st and ch == "..":
                st.pop()
        return "/" + "/".join(st)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.simplifyPath("/home/"), "/home")
        self.assertEqual(obj.simplifyPath("/../"), "/")
        self.assertEqual(obj.simplifyPath("/home//foo/"), "/home/foo")
        self.assertEqual(obj.simplifyPath("/a/./b/../../c/"), "/c")


if __name__ == "__main__":
    unittest.main()
