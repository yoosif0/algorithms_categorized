"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
deeedbbcccbdaa
d[1]
e[3]

"""
import unittest


class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for ch in s:
            if not st or ch != st[-1]:
                st.append(ch)
            else:
                st.pop()
        return "".join(st)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.removeDuplicates("abbaca"), "ca")


if __name__ == "__main__":
    unittest.main()
