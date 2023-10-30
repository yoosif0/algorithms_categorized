"""
https://leetcode.com/problems/count-operations-to-obtain-zero/
#reach_target_number
"""
import unittest


class Solution:
    def countOperations(self, n: int, n2: int) -> int:
        ans = 0
        if not n2:
            return ans
        while n:
            if n >= n2:
                n -= n2
            else:
                n2 -= n
            ans += 1
        return ans


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.countOperations(2, 3), 3)
        self.assertEqual(t.countOperations(10, 10), 1)


if __name__ == "__main__":
    unittest.main()
