"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
0,0,0,0,0,1,1,1,2,2,3,3,4
l         r
0,1,0,0,0,1,1,1,2,2,3,3,4
  l


once element detected, move r to the next element and bypass duplicates
swap a[l+1] and a[r]
l = r, move r till you find another element

"""

import unittest


# O(1) space
class Solution:
    def removeDuplicates(self, a: list[int]) -> int:
        l = 1
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                pass
            else:
                a[l] = a[i]
                l += 1
        return l


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(obj.removeDuplicates([1]), 1)


if __name__ == "__main__":
    unittest.main()
