import unittest

"""
        1
       1,1
      1,2,1
     1,3,3,1
    1,4,6,4,1
   1,5,10,10,5,1
  1,6,15,20,15,6,1
 1,7,21,35,35,21,7,1
"""


def getSumArr(arr: list[int]) -> list[int]:
    sums = []
    for i in range(len(arr) - 1):
        sum = arr[i] + arr[i + 1]
        sums.append(sum)
    return sums


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows = [[1], [1, 1]]
        if numRows == 1:
            return rows[:1]
        if numRows == 2:
            return rows
        for i in range(2, numRows):
            newRow = [1] + getSumArr(rows[i - 1]) + [1]
            rows.append(newRow)
        return rows


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.generate(1), [[1]])
        self.assertEqual(
            t.generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        )


if __name__ == "__main__":
    unittest.main()
