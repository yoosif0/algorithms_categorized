"""
https://leetcode.com/problems/decode-string
popping point is when you meet a closing bracket. 
"""


import unittest


class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for ch in s:
            st.append(ch)
            # for more than one digit numbers or more than one char substrings
            if len(st) >= 2:
                if (st[-1].isdigit() and st[-2].isdigit()) or (
                    st[-1].islower() and st[-2].islower()
                ):
                    r, l = st.pop(), st.pop()
                    st.append(l + r)
            if st[-1] == "]":
                _, sub, _, n = st.pop(), st.pop(), st.pop(), st.pop()
                res = int(n) * sub
                st.append(res)
                # in case there is another substring evaluated before
                if len(st) >= 2 and st[-2].islower():
                    r, l = st.pop(), st.pop()
                    st.append(l + r)
        return st[0]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.decodeString("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(t.decodeString("3[a]11[b]"), "aaabbbbbbbbbbb")
        self.assertEqual(t.decodeString("3[a2[c]3[d]]2[f]"), "accdddaccdddaccdddff")
        self.assertEqual(t.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(
            t.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"),
            "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef",
        )


if __name__ == "__main__":
    unittest.main()
