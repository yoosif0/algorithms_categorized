"""
"""

import unittest


class Solution:
    def sortArray(self, a: list[int]) -> list[int]:
        if not a:
            return []
        p = a[0]
        # 3 arrays for whether the element is less than, greater than, or equal to pivot
        l = []
        r = []
        s = []
        for i in range(1, len(a)):
            if a[i] > a[0]:
                r.append(a[i])
            elif a[i] < a[0]:
                l.append(a[i])
            else:
                s.append(a[i])
        return [*self.sortArray(l), p, *s, *self.sortArray(r)]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.sortArray([5, 2, 3, 1]), [1, 2, 3, 5])


if __name__ == "__main__":
    unittest.main()
