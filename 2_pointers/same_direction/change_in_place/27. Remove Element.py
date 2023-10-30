"""
https://leetcode.com/problems/remove-element/
"""
import unittest


class Solution:
    def removeElement(self, a: list[int], val: int) -> int:
        l = 0
        for i in a:
            if i != val:
                a[l] = i
                l += 1
        return l


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.removeElement([3, 2, 2, 3], 3), 2)
        self.assertEqual(obj.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
        self.assertEqual(obj.removeElement([2], 3), 1)
        self.assertEqual(obj.removeElement([1], 1), 0)
        self.assertEqual(obj.removeElement([3, 2, 2, 3], 3), 2)


if __name__ == "__main__":
    unittest.main()
