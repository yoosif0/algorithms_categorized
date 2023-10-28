"""
https://leetcode.com/problems/split-with-minimum-sum/
#greedy

234567899

2468
3579

fill 2 arrays simultaneously
"""

import unittest


class Solution:
    def splitNum(self, n: int) -> int:
        a = sorted(str(n))
        a2 = []
        a3 = []
        i = 0
        while i < len(a) - 1:
            a2.append(a[i])
            a3.append(a[i + 1])
            i += 2
        if len(a) % 2 != 0:
            a2.append(a[i])
        return int("".join(a2)) + int("".join(a3))


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.splitNum(4325), 59)


if __name__ == "__main__":
    unittest.main()
