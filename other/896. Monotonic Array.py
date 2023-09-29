"""
https://leetcode.com/problems/monotonic-array
"""
import unittest


class Solution:
    def isMonotonic(self, a: list[int]) -> bool:
        # determine based on the first couple of nums whether the array should increase or decrease
        i = 1
        should_increase = True
        while i < len(a):
            if a[i] == a[0]:
                i += 1
            elif a[i] > a[0]:
                should_increase = True
                break
            else:
                should_increase = False
                break
        # based on whether it should increase or not, check the remaining numbers
        for j in range(i + 1, len(a)):
            if (a[j] >= a[j - 1] and should_increase) or (
                a[j] <= a[j - 1] and not should_increase
            ):
                pass
            else:
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
