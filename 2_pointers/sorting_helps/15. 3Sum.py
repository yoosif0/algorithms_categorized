"""
https://leetcode.com/problems/3sum/
Sorting here helps us here have 2 pointers. Edge cases here involves not duplicating a set. We do this
by skipping i if it points to a same number as a[i-1] and the same thing with l.
"""


import unittest


class Solution:
    def threeSum(self, a: list[int]) -> list[list[int]]:
        ans = []
        a.sort()
        for i in range(len(a)):
            # skipping repititive a[i]
            if i >= 1 and a[i] == a[i - 1]:
                continue
            l = i + 1
            r = len(a) - 1
            target = -a[i]
            while l < r:
                # skipping repititve a[l]
                if l != i + 1 and a[l] == a[l - 1]:
                    l += 1
                    # need to get off the while loop to check that l is not equal to r
                    continue
                sum = a[l] + a[r]
                if sum == target:
                    ans.append([a[i], a[l], a[r]])
                    l += 1
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(t.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(t.threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
        self.assertEqual(
            t.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]),
            [
                [-4, 0, 4],
                [-4, 1, 3],
                [-3, -1, 4],
                [-3, 0, 3],
                [-3, 1, 2],
                [-2, -1, 3],
                [-2, 0, 2],
                [-1, -1, 2],
                [-1, 0, 1],
            ],
        )


if __name__ == "__main__":
    unittest.main()
