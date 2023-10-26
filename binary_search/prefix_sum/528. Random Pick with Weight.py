"""
https://leetcode.com/problems/random-pick-with-weight
#prefix_sum
[1,3,9]
tot=13
random from 1 to 13. If the number is 1 return 1 if the number is 2,3,4 return 3. If the number is 5,6,7,8,9,10,11,12,13 
return 13. 
[1,4,13] left bisect
"""
import bisect
import random
import unittest


class Solution:
    def __init__(self, a: list[int]):
        for i in range(1, len(a)):
            a[i] += a[i - 1]
        self.a = a

    def pickIndex(self) -> int:
        n = random.randint(1, self.a[-1])
        return bisect.bisect_left(self.a, n)


class Test(unittest.TestCase):
    def test(self):
        # t = Solution([1, 3])
        t = Solution([3, 14, 1, 7])
        print(t.pickIndex())
        print(t.pickIndex())
        print(t.pickIndex())
        print(t.pickIndex())
        print(t.pickIndex())
        print(t.pickIndex())
        print(t.pickIndex())
        print(t.pickIndex())
        print(t.pickIndex())


if __name__ == "__main__":
    unittest.main()
