"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
import unittest

operations_set = set({"+", "-", "*", "/"})


def str_to_op(num1: int, num2: int, op: str):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2
    else:
        return int(num1 / num2)


class Solution:
    def evalRPN(self, a: list[str]) -> int:
        st = []
        for ch in a:
            if ch not in operations_set:
                st.append(int(ch))
            else:
                ppd = int(st.pop())
                ppd2 = int(st.pop())
                result = str_to_op(ppd2, ppd, ch)
                st.append(result)
        return st[-1]


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
