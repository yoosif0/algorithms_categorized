"""
https://leetcode.com/problems/crawler-log-folder/
"""

import unittest


class Solution:
    def minOperations(self, a: list[str]) -> int:
        cnt = 0
        for ch in a:
            if ch == "../":
                cnt = cnt - 1 if cnt > 0 else cnt
            elif ch == "./":
                pass
            else:
                cnt += 1
        return cnt


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.minOperations(["d1/", "d2/", "../", "d21/", "./"]), 2)


if __name__ == "__main__":
    unittest.main()
