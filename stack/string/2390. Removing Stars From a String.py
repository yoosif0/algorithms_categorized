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

    # def removeStars(self, s: str) -> str:
    #     ans = deque([])
    #     r = len(s) - 1
    #     jmp = 0
    #     while True:
    #         if r < 0:
    #             break
    #         elif s[r] == "*":
    #             jmp += 1
    #         elif jmp:
    #             jmp -= 1
    #         else:
    #             ans.appendleft(s[r])
    #         r -= 1
    #     return "".join(ans)

    # def removeStars(self, s: str) -> str:
    #     x = 0
    #     indecis_set = set()
    #     dq = deque([])
    #     for i in range(len(s) - 1, -1, -1):
    #         if s[i] == "*":
    #             indecis_set.add(i)
    #             x += 1
    #         elif x:
    #             indecis_set.add(i)
    #             x -= 1
    #         else:
    #             dq.appendleft(s[i])
    #     return "".join(dq)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.removeStars("leet**cod*e"), "lecoe")
        self.assertEqual(t.removeStars("erase*****"), "")


if __name__ == "__main__":
    unittest.main()
