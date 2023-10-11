"""
https://leetcode.com/problems/baseball-game/
"""
import unittest


class Solution:
    def calPoints(self, a: list[str]) -> int:
        st = []
        for ch in a:
            if ch == "+":
                st.append(int(st[-1]) + int(st[-2]))
            elif ch == "C":
                st.pop()
            elif ch == "D":
                st.append(int(st[-1]) * 2)
            else:
                st.append(int(ch))
        ans = 0
        for num in st:
            ans += int(num)
        return ans


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.calPoints(["5", "2", "C", "D", "+"]), 30)


if __name__ == "__main__":
    unittest.main()
