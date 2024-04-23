"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
"""

import unittest


class Solution:
    # O(nlogn)
    def canMakeArithmeticProgression(self, a: list[int]) -> bool:
        a.sort()
        d = a[1] - a[0]
        for i in range(2, len(a)):
            if (a[i] - a[i - 1]) != d:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.canMakeArithmeticProgression([1, 3, 5]), True)


if __name__ == "__main__":
    unittest.main()
