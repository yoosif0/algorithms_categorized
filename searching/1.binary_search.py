import unittest

class BinarySearch():
    def __init__(self, arr):
        self.arr = arr 

    def searchRecurs(self, val, low, high):
        mid = (high + low) // 2
        if high - low <= 1:
            return -1
        elif val == self.arr[mid]:
            return mid 
        elif val < self.arr[mid]:
            return self.searchRecurs(val, low, mid)
        else:
            return self.searchRecurs(val, mid, high)
        
    def search(self, val):
        lowIndex = 0
        highIndex = len(self.arr) - 1
        if val < self.arr[lowIndex] or val > self.arr[highIndex]:
            return -1
        if val == self.arr[highIndex]:
            return highIndex
        if val == self.arr[lowIndex]:
            return lowIndex
        return self.searchRecurs(val, lowIndex, highIndex )

class TestBinarySearch(unittest.TestCase):
    def test_simple(self):
        bs = BinarySearch([1,2,3,4,5,6,7,8,9]) 
        self.assertEqual(bs.search(4), 3)
        #  0 8 4     0 4 2     2 4 3
        self.assertEqual(bs.search(1), 0)
        self.assertEqual(bs.search(2), 1)
        self.assertEqual(bs.search(5), 4)
        self.assertEqual(bs.search(6), 5)
        self.assertEqual(bs.search(7), 6)
        self.assertEqual(bs.search(8), 7)
        self.assertEqual(bs.search(9), 8)

    def test_odd_number(self):
        bs = BinarySearch([1,2,3,4,5,6,7,8]) 
        self.assertEqual(bs.search(5), 4)
        #  0 7 3     3 7 5    3 5 4

    def test_outer(self):
        bs = BinarySearch([1,2,3,4,5,6,7,8,9]) 
        self.assertEqual(bs.search(20), -1)
        self.assertEqual(bs.search(0), -1)

    def test_not_exist_inner(self):
        bs = BinarySearch([1,2,3,3,5,6,7,8,9]) 
        self.assertEqual(bs.search(4), -1)
        #  0 8 4     0 4 2     2 4 3   3 4 



if __name__ == '__main__':
    unittest.main()