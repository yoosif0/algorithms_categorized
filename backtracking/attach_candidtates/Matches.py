"""
      1             2                 3
1,2,2,3,4,5,6    1,2,3,4,5,6      1,2,3,4,5,6

1,1,2,2,3,4,4,4,5,5,5,5,6,6,10,17
17,3
10,5,5
6,6,4,2,2
1,1,4,4,5,5

Try to make 20 from 1 item.
Then try with 2 values (nested loop). 
Then try with 3 values, etc, etc, etc

randomly accumulate till you reach s/4. Then do this 2 other times. The last side is for sure there since it's candidates is whatever is remaining

This reminds me of 2sum and 3sum but now it's UnknownSum. You don't know how many items will form the side
"""

import unittest


class Solution:
    def ansss(self, a: list[int]) -> list[list[int]]:
        s = sum(a)
        if s % 4 != 0:
            return False
        side = s // 4
        print("side has a length of:", side)
        solved = 0
        memo = set()
        def dfs(tmp: list[int], cs: list[int]):
            dd = []
            dd.append(tmp)
            dd.append(cs)
            nonlocal solved
            tmp.sort()
            cs.sort()
            key = str(str(tmp)+" "+str(cs))
            inmemo = key in memo
            if not inmemo:
                memo.add(key)
            cur = sum(tmp)
            if inmemo:
                dd.append("inmemo")
                return
            elif cur > side:
                dd.append("overflow")
                dfs(tmp[1:], cs+[tmp[0]])
            elif cur == side:
                dd.append("solvvved")
                solved += 1
                dfs([],cs)
            else:
                if len(cs):
                    dfs([*tmp,cs[0]], cs[1:])
            print(dd)
        dfs([a[0]], a[1:])
        print("solved times: ", solved)
        return solved == 4

a = [
    # [[1,2,1,2,2], True ],
    # [[3,3,3,3,4], False],
    [[1,1,2,2,3,4,4,4,5,5,5,5,6,6,10,17], True],
    # [[2,3,4,4,4,5,5,5,5,6,6,10,13], False]
]

class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        for case in a:
            print(case[1])
            self.assertEqual(t.ansss(case[0]), case[1])


if __name__ == "__main__":
    unittest.main()
