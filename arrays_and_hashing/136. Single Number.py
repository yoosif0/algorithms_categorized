"""
https://leetcode.com/problems/single-number/
"""
import unittest


class Solution:
    def singleNumber(self, a: list[int]) -> int:
        s = set()
        s2 = set()
        for i in range(len(a)):
            if a[i] in s2:
                continue
            elif a[i] in s:
                s2.add(a[i])
                s.remove(a[i])
            else:
                s.add(a[i])
        return list(s)[0]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.singleNumber([2, 2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
