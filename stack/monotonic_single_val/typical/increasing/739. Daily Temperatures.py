"""
https://leetcode.com/problems/daily-temperatures/
73,74,75,71,69,72,76,73
7:73 [(73,7)] ans 0
6:76 [(76,6)] pop 1 ans 0
5:72 [(76,6),(72,5)] ans 1
you pop when num is greater than or equal what's in stack. Stack should include something that represent time (not only value)
"""
import unittest


class Solution:
    def dailyTemperatures(self, a: list[int]) -> list[int]:
        st = []
        for i in range(len(a)):
            while st and a[i] > a[st[-1]]:
                ppd = st.pop()
                a[ppd] = i - ppd
            st.append(i)
        while st:
            a[st.pop()] = 0
        return a


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )
        self.assertEqual(
            obj.dailyTemperatures([30, 40, 50, 60]),
            [1, 1, 1, 0],
        )
        self.assertEqual(
            obj.dailyTemperatures([30, 60, 90]),
            [1, 1, 0],
        )


if __name__ == "__main__":
    unittest.main()
