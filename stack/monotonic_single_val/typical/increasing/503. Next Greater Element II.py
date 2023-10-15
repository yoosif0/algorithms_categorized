"""
https://leetcode.com/problems/next-greater-element-ii/
012
121

l = 0
st[1,2]

#circular

Here we can't overwrite the input arr because we loop twice
"""
import unittest


class Solution:
    def nextGreaterElements(self, a: list[int]) -> list[int]:
        st = []
        ans = [-1 for _ in range(len(a))]
        for i in range(len(a)):
            while st and a[i] > a[st[-1]]:
                ans[st.pop()] = a[i]
            st.append(i)
        # loop again but this time without pushing to st
        for i in range(len(a)):
            while st and a[i] > a[st[-1]]:
                ans[st.pop()] = a[i]
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.nextGreaterElements([1, 2, 1]),
            [2, -1, 2],
        )
        self.assertEqual(
            obj.nextGreaterElements([1, 2, 3, 4, 3]),
            [2, 3, 4, -1, 4],
        )
        self.assertEqual(
            obj.nextGreaterElements([5, 4, 3, 2, 1]),
            [-1, 5, 5, 5, 5],
        )


if __name__ == "__main__":
    unittest.main()
