"""
https://leetcode.com/problems/simplify-path/
#string
"""

import unittest


class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = []
        splitted = path.split("/")
        for thing in splitted:
            if thing == "..":
                if not folders:
                    continue
                folders.pop()
            elif len(thing) == 0 or thing == ".":
                continue
            else:
                folders.append(thing)
        return "/" + "/".join(folders)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.simplifyPath("/home/"), "/home")
        self.assertEqual(obj.simplifyPath("/../"), "/")
        self.assertEqual(obj.simplifyPath("/home//foo/"), "/home/foo")
        self.assertEqual(obj.simplifyPath("/a/./b/../../c/"), "/c")


if __name__ == "__main__":
    unittest.main()
