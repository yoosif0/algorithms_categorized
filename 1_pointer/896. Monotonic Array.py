"""
https://leetcode.com/problems/monotonic-array
"""
import unittest


class Solution:
    def isMonotonic(self, a: list[int]) -> bool:
        # determine based on the first couple of nums whether the array should increase or decrease
        fl = True
        i = 0
        while i < len(a) - 1 and a[i] == a[0]:
            i += 1
        if a[i] < a[0]:
            fl = False
        # check
        for i in range(1, len(a)):
            if a[i] != a[i - 1] and (a[i] >= a[i - 1]) != fl:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isMonotonic([1, 2, 2, 3]), True)
        self.assertEqual(obj.isMonotonic([6, 5, 4, 4]), True)
        self.assertEqual(obj.isMonotonic([1, 3, 2]), False)
        self.assertEqual(obj.isMonotonic([1, 2, 5, 3, 3]), False)


if __name__ == "__main__":
    unittest.main()
