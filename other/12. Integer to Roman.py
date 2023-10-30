"""
https://leetcode.com/problems/integer-to-roman/
"""
import unittest


class Solution:
    def intToRoman(self, n: int) -> str:
        d = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        s = ""
        for k in d:
            while n > 0 and k <= n:
                n -= k
                s += d[k]
        return s


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.intToRoman(3), "III")
        self.assertEqual(obj.intToRoman(58), "LVIII")
        self.assertEqual(obj.intToRoman(1994), "MCMXCIV")


if __name__ == "__main__":
    unittest.main()
