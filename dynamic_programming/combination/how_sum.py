"""
https://www.youtube.com/watch?v=oBt53YbR9Kk
[5,3,4,7,2,1,9,89,2,6] 8
0: r=3, check if contains 3


"""
import unittest
import functools
from typing import Optional


class Solution:
    def howSum(self, target: int, numbers: list[int]) -> Optional[list[int]]:
        @functools.cache
        def recursHowSum(target: int) -> Optional[list[int]]:
            if target == 0:
                return []
            if target < 0:
                return None
            for i in range(len(numbers)):
                num = numbers[i]
                sol = recursHowSum(target - num)
                if sol is not None:
                    sol.append(num)
                    return sol
            return None

        return recursHowSum(target)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.howSum(7, [2, 3]), [3, 2, 2])
        self.assertEqual(t.howSum(7, [5, 3, 4, 7]), [4, 3])
        self.assertEqual(t.howSum(7, [2, 4]), None)
        self.assertEqual(t.howSum(300, [7, 14]), None)


if __name__ == "__main__":
    unittest.main()
