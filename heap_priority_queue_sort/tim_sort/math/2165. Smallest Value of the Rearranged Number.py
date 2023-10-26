"""
https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
5706   
7650

if 0 is the first, just substiue. sort reverse when n<0
#math
"""

import unittest


class Solution:
    def smallestNumber(self, n: int) -> int:
        a = sorted(str(abs(n)), reverse=n < 0)
        if a[0] == "0" and n > 0:
            i = 1
            while i < len(a) and a[i] == "0":
                i += 1
            a[0], a[i] = a[i], a[0]
        a = int("".join(a))
        return a if n > 0 else -a


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.smallestNumber(310), 103)
        self.assertEqual(t.smallestNumber(3010), 1003)
        self.assertEqual(t.smallestNumber(-7605), -7650)


if __name__ == "__main__":
    unittest.main()
