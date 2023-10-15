"""
https://leetcode.com/problems/remove-k-digits/
"""
from collections import deque
import unittest


class Solution:
    def removeKdigits(self, a: str, k: int) -> str:
        st = deque([])
        for i in range(len(a)):
            while st and a[i] < st[-1] and k:
                st.pop()
                k -= 1
            st.append(a[i])
        while k > 0:
            st.pop()
            k -= 1
        while st and st[0] == "0":
            st.popleft()
        if not st:
            return "0"
        return "".join(st)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.removeKdigits("1432219", 3), "1219")
        self.assertEqual(obj.removeKdigits("10200", 1), "200")
        self.assertEqual(obj.removeKdigits("10", 2), "0")
        self.assertEqual(obj.removeKdigits("129", 2), "1")
        self.assertEqual(obj.removeKdigits("9", 1), "0")
        self.assertEqual(obj.removeKdigits("10", 1), "0")


if __name__ == "__main__":
    unittest.main()
