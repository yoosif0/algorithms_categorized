"""
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""
import unittest
import functools
from typing import Optional


class Solution:
    def bestSum(self, target: int, numbers: list[int]) -> Optional[list[int]]:
        @functools.cache
        def recursHowSum(target: int) -> Optional[list[int]]:
            ans = None
            if target == 0:
                return []
            if target < 0:
                return None
            for i in range(len(numbers)):
                num = numbers[i]
                remainder_combination = recursHowSum(target - num)
                if remainder_combination is not None:
                    combination = remainder_combination + [num]
                    if ans is None or len(ans) > len(remainder_combination):
                        ans = combination
            return ans

        return recursHowSum(target)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.bestSum(7, [5, 3, 4, 7]), [7])
        self.assertEqual(t.bestSum(8, [2, 3, 5]), [3, 5])
        self.assertEqual(t.bestSum(8, [1, 4, 5]), [4, 4])
        self.assertEqual(t.bestSum(100, [1, 2, 5, 25]), [25, 25, 25, 25])


if __name__ == "__main__":
    unittest.main()
