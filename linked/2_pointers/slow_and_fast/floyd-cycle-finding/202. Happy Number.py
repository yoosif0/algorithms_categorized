"""
https://leetcode.com/problems/happy-number/
The idea here is to keep computing over and over and over till we reach the number 1. But how many loops should
we perform till we know we're not converging to 1? We'll use floyd cycle finder algorithm to do this. When the 
slow and fast pointers have the same value, we know that the cycle is circular so there is no need to loop further.
"""
import unittest


def compute(n: int):
    arr = [int(char) for char in str(n)]
    n = 0
    for num in arr:
        n += pow(num, 2)
    return n


class Solution:
    def isHappy(self, n: int) -> bool:
        s = f = n
        while True:
            s = compute(s)
            f = compute(compute(f))
            if s == 1 or f == 1:
                return True
            if s == f:
                return False


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.isHappy(1), True)
        self.assertEqual(obj.isHappy(19), True)
        self.assertEqual(obj.isHappy(2), False)
        self.assertEqual(obj.isHappy(10), True)


if __name__ == "__main__":
    unittest.main()
