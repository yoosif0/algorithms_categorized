"""
https://leetcode.com/problems/palindrome-number/
to make it faster we reverse only half the number. We shift digits from x to y by multiplying y by 10 and adding remainder of dividing x by 10
#remove_digits


15951
1595   1
159    1*10+5
15     15*10+9

25952
2595    2
259     2*10+5

10
1     0
"""

import unittest


# this solution is little bit complex for speed. it can be solved in a much easier way
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # edge cases like 10 and -5
        if x < 0 or x != 0 and x % 10 == 0:
            return False
        y = 0
        while x > y:
            # x%10 is the remainder
            y = y * 10 + x % 10
            x = x // 10
        # we are accounting for both types of palindromes (even and odd number of digits as centers)
        return x == y or x == y // 10


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.isPalindrome(121), True)
        self.assertEqual(t.isPalindrome(10), False)
        self.assertEqual(t.isPalindrome(0), True)


if __name__ == "__main__":
    unittest.main()
