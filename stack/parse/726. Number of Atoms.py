"""
https://leetcode.com/problems/number-of-atoms/
The popping instance is when we find a closing bracket
"""


from collections import Counter
import unittest


class Solution:
    def countOfAtoms(self, s: str) -> str:
        st = []
        i = 0
        while i < len(s):
            if s[i].isupper():
                el = s[i]
                n = ""
                # check if it's multi-char
                i += 1
                while i < len(s) and s[i].islower():
                    el += s[i]
                    i += 1
                # get numbers of this atom
                while i < len(s) and s[i].isdigit():
                    n += s[i]
                    i += 1
                n = int(n) if n.isdigit() else 1
                st.append((el, n))
            elif s[i] == "(":
                st.append(s[i])
                i += 1
            elif s[i] == ")":
                # get number
                i += 1
                n = ""
                while i < len(s) and s[i].isdigit():
                    n += s[i]
                    i += 1
                n = 1 if n == "" else int(n)
                # pop and append to arr till you reach the opening bracket
                a = []
                while st and st[-1] != "(":
                    a.append(st.pop())
                # pop opening bracket
                st.pop()
                # push back to stack after multiplying the number
                for j in range(len(a) - 1, -1, -1):
                    a[j] = (a[j][0], n * a[j][1])
                    st.append(a[j])
        # Count the number of atoms for each element using a counter
        m = Counter()
        for tup in st:
            m[tup[0]] += tup[1]
        # sort them by alphabatical order
        a = []
        for k in m:
            a.append((k, m[k]))
        a.sort(key=lambda x: x[0])
        # if number is one don't include it in ans array
        ans = []
        for tup in a:
            ans.append(tup[0])
            if tup[1] > 1:
                ans.append(str(tup[1]))
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.countOfAtoms("H2O"), "H2O")
        self.assertEqual(t.countOfAtoms("K4(ON(SO3)2)2"), "K4N2O14S4")
        self.assertEqual(t.countOfAtoms("Mg(OH)2"), "H2MgO2")
        self.assertEqual(t.countOfAtoms("(H)"), "H")


if __name__ == "__main__":
    unittest.main()
