"""
https://leetcode.ca/all/360.html
#math

The trick here to know that a quadratic function either has a peak or a valley. 

a<0 => peak => fill array from min to max (left to right)

a>0 => valley => 

"""

import unittest


# O(n) time and O(n) space
class Solution:
    def sort(self, a: list[int], a2, b, c) -> list[int]:
        l = 0
        r = len(a) - 1
        a = [a2 * n**2 + b * n + c for n in a]
        ans = [None for _ in range(len(a))]
        if a2 < 0:
            for i in range(len(ans)):
                if a[r] < a[l]:
                    ans[i] = a[r]
                    r -= 1
                else:
                    ans[i] = a[l]
                    l += 1
        else:
            for i in range(len(ans) - 1, -1, -1):
                if a[r] > a[l]:
                    ans[i] = a[r]
                    r -= 1
                else:
                    ans[i] = a[l]
                    l += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sort([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        self.assertEqual(t.sort([-4, -2, 2, 4], -1, 3, 5), [-23, -5, 1, 7])
        self.assertEqual(t.sort([-4, -2, 2, 4], 1, 0, 0), [4, 4, 16, 16])


if __name__ == "__main__":
    unittest.main()
