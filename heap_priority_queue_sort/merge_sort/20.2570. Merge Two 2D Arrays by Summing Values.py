"""
https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
[[1,2],[2,3],[4,5]] [[1,4],[3,2],[4,1]]
               l                   r
after summing and appending push both pointers to the right
if l_id < r_id:
    append l_item
    l+=1
elif l_id > r_id:
    append r_item
    r+=1
else:
    append sum
    r+=1
    l+=1
[[1,6],[2,3],[3,2],[4,6]] 
Output: [[1,6],[2,3],[3,2],[4,6]]
"""

import unittest


class Solution:
    def mergeArrays(self, a: list[list[int]], a2: list[list[int]]) -> list[list[int]]:
        ans = []
        l = r = 0
        while l < len(a) and r < len(a2):
            if a[l][0] < a2[r][0]:
                ans.append(a[l])
                l += 1
            elif a[l][0] > a2[r][0]:
                ans.append(a2[r])
                r += 1
            else:
                ans.append([a[l][0], a[l][1] + a2[r][1]])
                r += 1
                l += 1
        # fill with a if ptr did not reach end
        while l < len(a):
            ans.append(a[l])
            l += 1
        # fill with a2 if ptr did not reach end
        while r < len(a2):
            ans.append(a2[r])
            r += 1
        return ans


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(
            t.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]),
            [[1, 6], [2, 3], [3, 2], [4, 6]],
        )


if __name__ == "__main__":
    unittest.main()
