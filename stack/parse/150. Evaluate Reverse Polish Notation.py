"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
The popping instance is when we have an operation
"""
import unittest

ops = set({"+", "-", "*", "/"})


def arith(op: str, n2: int, n1: int):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    else:
        return int(n1 / n2)


class Solution:
    def evalRPN(self, a: list[str]) -> int:
        st = []
        for ch in a:
            st.append(ch)
            if ch in ops:
                ans = arith(st.pop(), int(st.pop()), int(st.pop()))
                st.append(ans)
        return int(st[-1])


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(obj.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(
            obj.evalRPN(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22,
        )


if __name__ == "__main__":
    unittest.main()
