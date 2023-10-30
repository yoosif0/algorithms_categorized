"""
https://leetcode.com/problems/single-number/
"""
import unittest


class Solution:
    def singleNumber(self, a: list[int]) -> int:
        ans = set()
        s = set()
        for i in range(len(a)):
            if a[i] in s:
                continue
            elif a[i] in ans:
                s.add(a[i])
                ans.remove(a[i])
            else:
                ans.add(a[i])
        return list(ans)[0]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.singleNumber([2, 2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
