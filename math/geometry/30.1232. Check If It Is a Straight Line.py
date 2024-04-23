"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""

import unittest


class Solution:
    def checkStraightLine(self, a: list[int]) -> bool:
        xd = a[1][0] - a[0][0]
        if xd == 0:
            for i in range(2, len(a)):
                xd2 = a[i][0] - a[i - 1][0]
                if xd2 != 0:
                    return False
        else:
            m = (a[1][1] - a[0][1]) / xd
            for i in range(2, len(a)):
                xd = a[i][0] - a[i - 1][0]
                if xd == 0:
                    return False
                m2 = (a[i][1] - a[i - 1][1]) / xd
                if m2 != m:
                    return False
        return True


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]),
            True,
        )
        self.assertEqual(obj.checkStraightLine([[0, 0], [0, 1], [0, -1]]), True)
        self.assertEqual(obj.checkStraightLine([[1, 1], [2, 2], [2, 0]]), False)


if __name__ == "__main__":
    unittest.main()
