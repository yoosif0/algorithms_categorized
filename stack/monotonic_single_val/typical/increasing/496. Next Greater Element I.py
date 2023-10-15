"""
https://leetcode.com/problems/next-greater-element-i/
"""
import unittest


class Solution:
    def nextGreaterElement(self, req: list[int], a: list[int]) -> list[int]:
        st = []
        m = {}
        for i in range(len(a)):
            while st and a[i] > a[st[-1]]:
                m[a[st.pop()]] = a[i]
            st.append(i)
        while st:
            m[a[st.pop()]] = -1
        for i, n in enumerate(req):
            req[i] = m[n]
        return req


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(
            obj.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]),
            [-1, 3, -1],
        )


if __name__ == "__main__":
    unittest.main()
