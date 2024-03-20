"""
1   2    3               2    5    6
            i                 j

1 2 2 3 _ _
"""

import unittest


class Solution:
    def merge(self, a: list[int], a2: list[int]) -> None:
        ans = [None for _ in range(len(a) + len(a2))]
        p , p2 = 0, 0
        for i in range(len(ans)):
            if p >= len(a) or a2[p2] < a[p] :
                ans[i] = a2[p2]
                p2 +=1
            else:
                ans[i] = a[p]
                p +=1
        return ans



class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.merge([1, 2, 3], [2, 5, 6]), [1, 2, 2, 3, 5, 6]
        )

if __name__ == "__main__":
    unittest.main()
