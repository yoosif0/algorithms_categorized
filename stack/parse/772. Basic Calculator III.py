"""
https://leetcode.com/problems/basic-calculator-iii/
https://leetcode.ca/all/772.html
https://www.lintcode.com/problem/849/

"""
from collections import deque
import unittest

hi = set(["*", "/"])
lo = set(["+", "-"])
op_set = lo.union(hi)


def arith(op: str, n1: int, n2: int):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    else:
        return int(n1 / n2)


# takes [5, "+", 2, "*", 1]
def solve_arith(a: list) -> int:
    # solve multiplication and division (hi priority)
    st = []
    for ch in a:
        st.append(ch)
        while len(st) >= 2 and st[-1] not in hi and st[-2] in hi:
            n2, op, n1 = st.pop(), st.pop(), st.pop()
            st.append(arith(op, n1, n2))
    return solve_lo(st)


# takes [5, "+", 2]
def solve_lo(a: list):
    # solve addition and subraction (lo priority)
    st = []
    for ch in a:
        st.append(ch)
        while len(st) >= 2 and st[-1] not in lo and st[-2] in lo:
            n2, op, n1 = st.pop(), st.pop(), st.pop()
            ans = arith(op, n1, n2)
            st.append(ans)
    return st[0]


# remove spaces and append digits together
def cleanup(s):
    a = []
    fl = False
    for ch in s:
        if ch == " ":
            continue
        # handle numbers
        if ch.isdigit():
            # if number is just another digit, append to last item in arr
            num = int(ch) if not fl else a.pop() * 10 + int(ch)
            a.append(num)
            fl = True
        else:
            a.append(ch)
            fl = False
    return a


class Solution:
    def calculate(self, s: str) -> int:
        a = deque(cleanup(s))
        a.appendleft("(")
        a.append(")")
        st = deque([])
        for ch in a:
            st.append(ch)
            if ch == ")":
                # pop closing bracket
                st.pop()
                a2 = deque([])
                i = len(st) - 1
                while st and i < len(st) and st[-1] != "(":
                    a2.appendleft(st.pop())
                    i -= 1
                # pop opening bracket
                st.pop()
                st.append(solve_arith(a2))
        return st[-1]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.calculate("(2+6* 3+5- (3*14/7+2)*5)+3"), -12)


if __name__ == "__main__":
    unittest.main()
