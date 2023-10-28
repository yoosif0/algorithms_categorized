"""
https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
stream ->>>>>
st=[1]
<5 <8 <7 6> 30> 11> 25> 
"""

import unittest


class Solution:
    def fish(self, a, aa):
        st = []
        ans = 0
        for i in range(len(a)):
            if aa[i] == 1:
                st.append(a[i])
            else:
                fl = True
                while st:
                    if a[i] > st[-1]:
                        # eat other fish
                        st.pop()
                    else:
                        # a[i] die
                        fl = False
                        break
                ans += int(fl)
        return ans + len(st)


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.fish([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]), 2)
        self.assertEqual(t.fish([4, 3, 2, 1, 5], [0, 0, 0, 0, 0]), 5)
        self.assertEqual(t.fish([4, 3, 2, 1, 5], [1, 1, 1, 1, 1]), 5)
        self.assertEqual(
            t.fish(
                [1, 5, 8, 7, 6, 30, 11, 9, 10, 25, 22],
                [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
            ),
            7,
        )
        self.assertEqual(t.fish([5], [0]), 1)
        self.assertEqual(t.fish([3], [1]), 1)
        self.assertEqual(t.fish([4, 5], [0, 1]), 2)
        self.assertEqual(t.fish([5, 4], [0, 1]), 2)


if __name__ == "__main__":
    unittest.main()
