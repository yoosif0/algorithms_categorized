
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

