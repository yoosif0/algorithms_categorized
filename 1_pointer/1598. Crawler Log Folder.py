"""
https://leetcode.com/problems/crawler-log-folder/
"""

import unittest


class Solution:
    def minOperations(self, a: list[str]) -> int:
        ans = 0
        for ch in a:
            if ch == "../":
                ans = ans - 1 if ans > 0 else ans
            elif ch == "./":
                pass
            else:
                ans += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.minOperations(["d1/", "d2/", "../", "d21/", "./"]), 2)


if __name__ == "__main__":
    unittest.main()
