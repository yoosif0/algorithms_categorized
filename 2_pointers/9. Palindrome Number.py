"""
https://leetcode.com/problems/palindrome-number/
"""

import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = []
        while x > 0:
            a.append(x % 10)
            x = x // 10
        l = 0
        r = len(a) - 1
        while l <= r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.isPalindrome(121), True)
        self.assertEqual(t.isPalindrome(10), False)


if __name__ == "__main__":
    unittest.main()
