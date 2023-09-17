"""
https://leetcode.com/problems/insert-interval/
[[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


assume I have 2 intervals to be removed before and 3 intervals to be removed after, I grab the  starting point and ending point
from last element in arr in both arrays by setting max() and min()
I set the new index as index -len(to_be_removed), 


[[6,9], [12,15]], newInterval = [0,1]

[[6,9], [12,15]], newInterval = [10,11]



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]


"""
import unittest


class Solution:
    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        if not intervals:
            return [new_interval]
        if not new_interval:
            return intervals

        i = 0
        ans = []

        # fill initial portion of ans
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            ans.append(intervals[i])
            i += 1

        # fill problematic portion
        to_insert_start = new_interval[0]
        to_insert_end = new_interval[1]
        while i < len(intervals) and intervals[i][0] <= to_insert_end:
            to_insert_start = min(intervals[i][0], to_insert_start)
            to_insert_end = max(intervals[i][1], to_insert_end)
            i += 1
        ans.append([to_insert_start, to_insert_end])

        # fill rest of unproblematic array
        for j in range(i, len(intervals)):
            ans.append(intervals[j])
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.insert([[6, 9], [12, 15]], [10, 11]),
            [[6, 9], [10, 11], [12, 15]],
        )
        self.assertEqual(t.insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(
            t.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            [[1, 2], [3, 10], [12, 16]],
        )
        self.assertEqual(t.insert([], [2, 5]), [[2, 5]])
        self.assertEqual(t.insert([[2, 5]], []), [[2, 5]])
        self.assertEqual(t.insert([[1, 5]], [6, 8]), [[1, 5], [6, 8]])


if __name__ == "__main__":
    unittest.main()
