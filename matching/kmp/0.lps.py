"""
LPS stands for longest prefix suffix
"""

import unittest

"""
01001201222223
aabxaayaaaaaab
 j       i
"""


def createLPS(s: str):
    dp = [0 for _ in range(len(s))]
    j = 0
    i = 1
    while i < len(s):
        if s[j] == s[i]:
            dp[i] = j + 1
            i += 1
            j += 1
        elif j != 0:
            j = dp[j - 1]
        else:
            dp[i] = 0
            i += 1
    return dp


class Test(unittest.TestCase):
    def test(self):
        # self.assertEqual(createLPS("aabxaayaab"), [0, 1, 0, 0, 1, 2, 0, 1, 2, 3])
        # self.assertEqual(
        #     createLPS("aaacecaa_aacecaaa"),
        #     [0, 1, 2, 0, 0, 0, 1, 2, 0, 1, 2, 0, 0, 0, 1, 2, 3],
        # )
        self.assertEqual(
            createLPS("abababc_ababc"),
            [0, 0, 1, 2, 3, 4, 0, 0, 1, 2, 3, 4, 0],
        )
        print(createLPS("abab"))
        print(createLPS("aba"))
        print(createLPS("abcabcabcabc"))
        print(createLPS("abaababaab"))
        print(createLPS("a"))
        print(createLPS("cattigercat"))


if __name__ == "__main__":
    unittest.main()
