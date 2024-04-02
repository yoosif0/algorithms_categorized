"""
https://leetcode.com/problems/count-alternating-subarrays
#count_combinations
1,0,1,0,  1,  0,    1, 0,  1,  0,  0,  1,0,1,0,1
1 3 6 10 15  21    28  36 45  55  56  
"""

import unittest


class Solution:
    def countAlternatingSubarrays(self, a: list[int]) -> int:
        cur = 1
        stop = 0
        for i in range(1, len(a)):
            cur += 1  # subarray that contains only this element
            if a[i - 1] != a[i]:
                cur += i - stop  # subarrays for elements before this element
            else:
                stop = i
        return cur


class Test(unittest.TestCase):
    def test_numberOfSetBits(self):
        t = Solution()
        self.assertEqual(t.countAlternatingSubarrays([0, 1, 1, 1]), 5)
        self.assertEqual(t.countAlternatingSubarrays([1, 0, 1, 0]), 10)
        self.assertEqual(
            t.countAlternatingSubarrays(
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1]
            ),
            76,
        )


if __name__ == "__main__":
    unittest.main()
