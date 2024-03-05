"""
https://leetcode.com/problems/parse-lisp-expression/
"""
import unittest


def solve_let(a) -> int:
    m = {}
    i = 2
    st = []
    while i < len(a):
        # grab all variable declarations
        while i < len(a) and a[i] != :
            m[a[i]] = m[a[i + 1]]
            i += 2
        st.append(a[i])
        if a[i] == ")":
            if a[i - 2] == "add":
                _, n2, n1, _, _ = st.pop(), st.pop(), st.pop(), st.pop(), st.pop()
                st.append((0, n2, n1))
            elif a[i - 2] == "mult":
                _, n2, n1, _, _ = st.pop(), st.pop(), st.pop(), st.pop(), st.pop()
                st.append((1, n2, n1))


class Solution:
    def evaluate(self, s: str) -> int:
        
        del s
        solve_let(a)
        return a[-1]


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"), 14)
        self.assertEqual(obj.evaluate("(let x 3 x 2 x)"), 2)
        self.assertEqual(obj.evaluate("(let x 1 y 2 x (add x y) (add x y))"), 5)

# a = []
#         i = 0
#         # cleanup to make a look like ["(", "let", "x", 2, "(", "mult", "x", "(", "let", "x", 3, y, 4, "(", "add", "x", "y", ")", ")", ")", ")"]
#         while i < len(s):
#             if s[i] == "(" or s[i] == ")":
#                 a.append(s[i])
#                 i += 1
#             elif s[i] == " ":
#                 i += 1
#             else:
#                 s2 = s[i]
#                 i += 1
#                 while i < len(s) and s[i] != " " and s[i] != ")":
#                     s2 += s[i]
#                     i += 1
#                 a.append(s2)
if __name__ == "__main__":
    unittest.main()

"""
(let x 1 y 2 x (add x y) (add x y))
m:{x:1,y:2}

Let_args:[x,1,y,2,x,3]
"""
