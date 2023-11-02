"""
https://leetcode.com/problems/find-the-k-beauty-of-a-number
#numeric
#reverse_window
#count_subarrays
"""
from dataclasses import dataclass
import unittest

"""
430043 % 10 = 3
430043 / 10 = 43004
43004 % 10 = 4
43004 / 10 = 4300
4300 % 10 = 0
4300 / 10 = 430


r * 10 + w 
4 * 10 + 3 = 43

The trick to get O(1) space and O(n) time is to now how to have a numberice sliding window where you can add and remove digits. the sliding window here slides from right to left
"""


class Solution:
    def divisorSubstrings(self, n: int, k: int) -> int:
        n2 = n
        w_n = 0
        w_po = 0
        cnt = 0
        # initial w
        while w_po < k:
            w_n = w_n + (n2 % 10) * 10**w_po
            w_po += 1
            n2 = n2 // 10
        # slide w
        while True:
            if w_n != 0 and n % w_n == 0:
                cnt += 1
            # break when needed
            if n2 == 0:
                break
            # add to window
            w_n = w_n + (n2 % 10) * 10**w_po
            # remove from window
            w_n = w_n // 10
            n2 = n2 // 10
        return cnt


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.divisorSubstrings(430043, 2), 2)
        self.assertEqual(t.divisorSubstrings(240, 2), 2)
        self.assertEqual(t.divisorSubstrings(10, 1), 1)


if __name__ == "__main__":
    unittest.main()
