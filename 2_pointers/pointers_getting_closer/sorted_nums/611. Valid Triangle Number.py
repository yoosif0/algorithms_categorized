"""
https://leetcode.com/problems/valid-triangle-number/description/
a similar question in codility:
https://app.codility.com/programmers/lessons/15-caterpillar_method/count_triangles/
#triplets
"""
import unittest


class Solution:
    def triangleNumber(self, a: list[int]) -> int:
        pass


"""
1 2 5 8 10 12
l m        r
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.triangleNumber([10, 2, 5, 1, 8, 12]), 4)
        self.assertEqual(t.triangleNumber([2, 2, 3, 4]), 3)
        self.assertEqual(t.triangleNumber([4, 2, 3, 4]), 4)


if __name__ == "__main__":
    unittest.main()
