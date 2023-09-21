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
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        for i in range(0, len(tokens)):
            token = tokens[i]
            if token not in operations_set:
                num_stack.append(int(token))
            else:
                popped_1 = int(num_stack.pop())
                popped_2 = int(num_stack.pop())
                result = str_to_op(popped_2, popped_1, token)
                num_stack.append(result)
        return num_stack[-1]


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
