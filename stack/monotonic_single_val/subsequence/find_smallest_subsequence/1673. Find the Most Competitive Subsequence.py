"""
https://leetcode.com/problems/find-the-most-competitive-subsequence/
"""
import unittest


class Solution:
    def mostCompetitive(self, a: list[int], k: int) -> list[int]:
        st = []
        for i in range(len(a)):
            # do not pop if what's remaining is not enough
            while st and a[i] < st[-1] and len(a) - i > k - len(st):
                st.pop()
            st.append(a[i])
        while len(st) > k:
            st.pop()
        return st


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.mostCompetitive([3, 5, 2, 6], 2), [2, 6])
        self.assertEqual(obj.mostCompetitive([3, 5, 2, 6, 1], 2), [2, 1])
        self.assertEqual(obj.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4), [2, 3, 3, 4])
        self.assertEqual(
            obj.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 6), [2, 3, 3, 4, 9, 6]
        )


if __name__ == "__main__":
    unittest.main()
