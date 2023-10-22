"""
https://leetcode.com/problems/top-k-frequent-elements/
To have O(n) time, you don't sort. Instead you bucket sort

#bucket_sort
"""


from typing import Dict
import unittest


# O(n)
class Solution:
    def topKFrequent(self, a: list[int], k: int) -> list[int]:
        # num counter
        m = {}
        top = 0
        for i in range(len(a)):
            m[a[i]] = m.get(a[i], 0) + 1
            top = max(top, m[a[i]])

        # freq to nums
        m2 = {}
        for num in m:
            if m[num] not in m2:
                m2[m[num]] = []
            m2[m[num]].append(num)

        ans = []
        for i in range(top, 0, -1):
            if i not in m2:
                continue
            for j in range(len(m2[i])):
                ans.append(m2[i][j])
            if len(ans) == k:
                break
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(obj.topKFrequent([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
