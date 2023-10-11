"""
https://leetcode.com/problems/removing-stars-from-a-string/
#jmp
#back_to_front
#backspace
#solvable_stack_pointers

"""
from collections import deque
import unittest


class Solution:
    def removeStars(self, s: str) -> str:
        ans = deque([])
        r = len(s) - 1
        jmp = 0
        while True:
            if r < 0:
                break
            elif s[r] == "*":
                jmp += 1
            elif jmp:
                jmp -= 1
            else:
                ans.appendleft(s[r])
            r -= 1
        return "".join(ans)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.removeStars("leet**cod*e"), "lecoe")
        self.assertEqual(t.removeStars("erase*****"), "")


if __name__ == "__main__":
    unittest.main()
