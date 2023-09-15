"""
[2,3,1,5,7] 11
2: loop to find target 9 then 7 then 5 then 3 then 1 then -1. then 6 (9-3) then 4 then 2 then 0
time complexity if not cached (BT) is n to the power m where n is array length and m is target sum 
"""
import unittest
import functools


class Solution:
    def canSum(self, target: int, numbers: list[int]) -> bool:
        @functools.cache
        def recursCanSum(target: int) -> bool:
            if target == 0:
                return True
            if target < 0:
                return False
            for i in range(len(numbers)):
                if recursCanSum(target - numbers[i]):
                    return True
            return False

        return recursCanSum(target)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.canSum(7, [2, 3]), True)
        self.assertEqual(t.canSum(300, [7, 14]), False)


if __name__ == "__main__":
    unittest.main()
