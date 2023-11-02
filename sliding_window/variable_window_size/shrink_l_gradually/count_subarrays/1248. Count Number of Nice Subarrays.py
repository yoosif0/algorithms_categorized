"""
https://leetcode.com/problems/count-number-of-nice-subarrays/
"""

import unittest


class Solution:
    def numberOfSubarrays(self, a: list[int], k: int) -> int:
        # initial w
        l = 0
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.partitionString("abacaba"), 4)
        self.assertEqual(t.partitionString("ssssss"), 6)


if __name__ == "__main__":
    unittest.main()
