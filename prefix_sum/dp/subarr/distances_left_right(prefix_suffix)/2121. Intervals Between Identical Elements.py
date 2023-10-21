"""
https://leetcode.com/problems/intervals-between-identical-elements/
#store_index
#store_all_indecis

            6 7 8 910111213
3,1,2,1,1,3,1,3,3,2,2,1
{1:[1,3,4,6,11], 2:{2,9,10}, 3:{0,         5,      7       ,8}}
{1:[1,4,8,14,25],2:[2,11,21],3:[0,         5,   2*2+5=9, 1*3+9=12  ]}  
                               [5+5*3=20,  2+1*3=5  ,1,0]
                               [0,5,9,12] 


[1,4,  8,            14,      25]
[0,3,4*2+3=11, 6*3+11=29, 11*4+29=73]


"""

import unittest


class Solution:
    def getDistances(self, a: list[int]) -> list[int]:
        # hashmap for each value and its indecis
        m = {}
        for i in range(len(a)):
            if a[i] not in m:
                m[a[i]] = []
            m[a[i]].append(i)
        for k, ia in m.items():
            # distances on the left side
            dp1 = [0 for _ in range(len(ia))]
            for i in range(1, len(ia)):
                dp1[i] = (ia[i] - ia[i - 1]) * i + dp1[i - 1]
            # distances on the right side
            dp2 = [0 for _ in range(len(ia))]
            for i in range(len(ia) - 2, -1, -1):
                dp2[i] = (ia[i + 1] - ia[i]) * (len(ia) - 1 - i) + dp2[i + 1]
            # answer is sum (right + left) distances
            for i in range(len(ia)):
                a[ia[i]] = dp1[i] + dp2[i]
        return a


class Test(unittest.TestCase):
    def test(self):
        obj = Solution()
        self.assertEqual(obj.getDistances([2, 1, 3, 1, 2, 3, 3]), [4, 2, 7, 2, 4, 4, 5])


# 2:[0,4]

if __name__ == "__main__":
    unittest.main()
