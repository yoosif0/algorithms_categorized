"""
https://leetcode.com/problems/roman-to-integer/
"""
import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        n = 0
        i = 0
        for key in d:
            while i < len(s) and s[i : i + len(key)] == key:
                n += d[key]
                i += len(key)
        return n


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.romanToInt("III"), 3)
        self.assertEqual(obj.romanToInt("LVIII"), 58)
        self.assertEqual(obj.romanToInt("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
