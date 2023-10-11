"""
https://leetcode.com/problems/removing-stars-from-a-string/
#jmp
#backspace
#solvable_stack_pointers

"""
import unittest


class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for ch in s:
            if ch != "*":
                st.append(ch)
            else:
                st.pop()
        return "".join(st)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.removeStars("leet**cod*e"), "lecoe")
        self.assertEqual(t.removeStars("erase*****"), "")


if __name__ == "__main__":
    unittest.main()
