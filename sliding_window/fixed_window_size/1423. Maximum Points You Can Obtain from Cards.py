"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
[100,40,17,9,73,75]
"""


import unittest


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        ans = 0
        cur_count = 0

        def add_to_cur_count(index: int):
            nonlocal cur_count
            cur_count += cardPoints[index]

        def remove_from_cur_count(index: int):
            nonlocal cur_count
            cur_count -= cardPoints[index]

        def update_ans_if_applicable():
            nonlocal ans
            ans = max(ans, cur_count)

        # initial window (right side)
        for i in range(-k, 0):
            add_to_cur_count(i)
        update_ans_if_applicable()

        # slide window to the right to comeback to index 0 in circular fashion
        for i in range(0, k):
            add_to_cur_count(i)
            remove_from_cur_count(i - k)
            update_ans_if_applicable()
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.maxScore([1, 2, 3, 4, 5, 6, 1], 3), 12)
        self.assertEqual(t.maxScore([2, 2, 2], 2), 4)
        self.assertEqual(t.maxScore([9, 7, 7, 9, 7, 7, 9], 7), 55)
        self.assertEqual(t.maxScore([100, 40, 17, 9, 73, 75], 3), 248)


if __name__ == "__main__":
    unittest.main()
