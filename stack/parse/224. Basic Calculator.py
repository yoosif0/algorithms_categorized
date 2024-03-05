"""
https://leetcode.com/problems/basic-calculator/
The popping instance is a closing bracket
"""
from collections import deque
import unittest

op_set = set(["+", "-"])


def arith(op: str, n1: int, n2: int) -> int:
    if op == "+":
        return n1 + n2
    else:
        return n1 - n2


# takes [5, "+", 2, "-", 1]
def solve(a: deque) -> int:
    # handle ["-", "3"] by appending-left a "0"
    if a[0] in op_set:
        a.appendleft(0)
    n1 = a[0]
    op = None
    n2 = None
    fl = True
    for i in range(1, len(a)):
        if fl:
            op = a[i]
        else:
            n2 = a[i]
            n1 = arith(op, n1, n2)
        fl = not fl
    return n1


class Solution:
    def calculate(self, s: str) -> int:
        a = []
        # remove spaces and append digits together
        for ch in s:
            if ch == " ":
                continue
            # handle numbers
            if ch.isdigit():
                # if number is just another digit, append to last item in arr
                if a and type(a[-1]) is int:
                    a[-1] = a[-1] * 10 + int(ch)
                else:
                    a.append(int(ch))
            else:
                a.append(ch)
        st = deque([])
        for ch in a:
            if ch == "-" and st and st[-1] == "-":
                st.pop()
                st.append("+")
            elif ch == ")":
                a = deque([])
                i = len(st) - 1
                while st and i < len(st) and st[-1] != "(":
                    a.appendleft(st.pop())
                    i -= 1
                # pop opening bracket
                st.pop()
                st.append(solve(a))
            else:
                st.append(ch)
        return solve(st)


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(solve(deque(["-", 2])), -2)
        self.assertEqual(solve(deque([2, "+", 3])), 5)
        self.assertEqual(solve(deque([2, "+", 3, "-", 1, "+", 2])), 6)
        self.assertEqual(obj.calculate("-2"), -2)
        self.assertEqual(obj.calculate("(-2)"), -2)
        self.assertEqual(obj.calculate("-(-2)"), 2)
        self.assertEqual(obj.calculate("-(2)"), -2)
        self.assertEqual(obj.calculate("-(2+3)"), -5)
        self.assertEqual(obj.calculate("1 + 1"), 2)
        self.assertEqual(obj.calculate(" 2-1 + 2 "), 3)
        self.assertEqual(obj.calculate("(1+(4+5+2)-3)+(6+8)"), 23)
        self.assertEqual(obj.calculate("(1+(4+5+2)-3)+(6+18)"), 33)
        self.assertEqual(obj.calculate("2147483647"), 2147483647)
        self.assertEqual(obj.calculate("0"), 0)
        self.assertEqual(obj.calculate("1-(  -2)"), 3)


if __name__ == "__main__":
    unittest.main()
