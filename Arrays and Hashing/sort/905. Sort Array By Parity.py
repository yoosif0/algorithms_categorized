"""
https://leetcode.com/problems/sort-array-by-parity
"""


from collections import deque
import unittest


class Solution:
    def sortArrayByParity(self, a: list[int]) -> list[int]:
        ans = deque([])
        for num in a:
            if num % 2 == 0:
                ans.appendleft(num)
            else:
                ans.append(num)
        return list(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.sortArrayByParity([3, 1, 2, 4]), [4, 2, 3, 1])


if __name__ == "__main__":
    unittest.main()
