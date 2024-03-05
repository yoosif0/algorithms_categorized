"""
https://leetcode.com/problems/basic-calculator-ii/
popping instance is when you see an operator 
"""
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


class Solution:
    def calculate(self, s: str) -> int:
        a = []
        # remove spaces and append digits together
        for ch in s:
            if ch == " ":
                continue
            # handle numbers
            if ch not in op_set:
                # if number is just another digit, append to last item in arr
                if a and a[-1] not in op_set:
                    a[-1] = a[-1] * 10 + int(ch)
                else:
                    a.append(int(ch))
            else:
                a.append(ch)
        # solve multiplication and division (hi priority)
        st = []
        for ch in a:
            st.append(ch)
            while len(st) >= 2 and st[-1] not in hi and st[-2] in hi:
                n2, op, n1 = st.pop(), st.pop(), st.pop()
                st.append(arith(op, n1, n2))
        # solve addition and subraction (lo priority)
        st2 = []
        for ch in st:
            st2.append(ch)
            while len(st2) >= 2 and st2[-1] not in lo and st2[-2] in lo:
                n2, op, n1 = st2.pop(), st2.pop(), st2.pop()
                st2.append(arith(op, n1, n2))
        return st2[0]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.calculate("3+2*2"), 7)
        self.assertEqual(obj.calculate(" 3/2 "), 1)
        self.assertEqual(obj.calculate(" 3+5 / 2 "), 5)


if __name__ == "__main__":
    unittest.main()
