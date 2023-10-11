"""
https://leetcode.com/problems/backspace-string-compare/
#jmp
#back_to_front
#backspace
#solvable_stack_pointers

we jump whenever we see a backspace
"""
import unittest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r = len(s) - 1
        r2 = len(t) - 1
        while True:
            jmp = 0
            while True:
                if r < 0:
                    break
                if s[r] == "#":
                    r -= 1
                    jmp += 1
                elif jmp:
                    r -= 1
                    jmp -= 1
                else:
                    break

            jmp2 = 0
            while True:
                if r2 < 0:
                    break
                if t[r2] == "#":
                    r2 -= 1
                    jmp2 += 1
                elif jmp2:
                    r2 -= 1
                    jmp2 -= 1
                else:
                    break

            if r < 0 and r2 < 0:
                return True
            if r < 0 or r2 < 0:
                return False
            if s[r] != t[r2]:
                return False
            r -= 1
            r2 -= 1


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.backspaceCompare("ab#c", "ad#c"), True)
        self.assertEqual(t.backspaceCompare("ab##", "c#d#"), True)


if __name__ == "__main__":
    unittest.main()
