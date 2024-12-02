import unittest
def prnt2d(x, left, top, width=1):
    def prntcell(x):
        print( f"{x}".center(width), end=" ")

    for v in left:
        width = max(width, len(v))
    for v in top:
        width = max(width, len(v))

    prntcell("")
    for ch in top:
        prntcell(ch)
    print("")
    for i in range(len(left)):
        prntcell(left[i])
        for ch in x[i]:
            prntcell(ch)
        print("")

# print 2d no labels
def p2dnl(x, width=1):
    def prntcell(x):
        print( f"{x}".center(width), end=" ")

    prntcell("")
    print("")
    for i in range(len(x)):
        for ch in x[i]:
            prntcell(ch)
        print("")


a = [
    [
        [
            [1, 550, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ],
       "!cat",
       "!c.t",
       3
    ]
]

class Test(unittest.TestCase):
    def test(self):
        for x in a:
            prnt2d(x[0], x[1], x[2], width=x[3])
        for x in a:
            p2dnl(x[0], width=x[3])
        
            
if __name__ == "__main__":
    unittest.main()
