"""

"""
import unittest
import functools


@functools.cache
def recursCanSum(target: int, num: int) -> bool:
    if target == 0:
        return True
    if target < 0:
        return False
    if recursCanSum(target - num, num):
        return True
    return False


class Solution:
    def canSum(self, target: int, num: int) -> bool:
        return recursCanSum(target, num)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.canSum(7, 2), False)
        self.assertEqual(t.canSum(6, 2), True)
        self.assertEqual(t.canSum(300, 2), True)
        self.assertEqual(t.canSum(100, 3), False)


if __name__ == "__main__":
    unittest.main()
