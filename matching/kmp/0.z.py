"""
a a b x a a y a a b
        i
"""

import unittest


class Solution:
    def z(self, s: str) -> int:
        z = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            cnt = 0
            for j in range(min(i, len(s) - i)):
                if s[j] == s[i + j]:
                    cnt += 1
                else:
                    break
            z[i] = cnt
        return z

    def z_dp(self, pat: str, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            # continue the pattern if possible
            v = dp[i - 1]
            if v > 0 and v < len(pat) and s[i] == pat[v]:
                dp[i] = v + 1
            # we might be starting a new pattern
            elif s[i] == pat[0]:
                dp[i] = 1
        return dp


"""
s a r a b 215 s a r a s a r a b c a b c s a r a b s a r d d a m a h m s a r a b s a r a b s s a r a b y w q o s a r 
              1 2 3 4  
# If there is already a pattern, try to complete it
"""


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        # self.assertEqual(t.z("aabxaayaab"), [0, 1, 0, 0, 2, 1, 0, 3, 1, 0])
        # self.assertEqual(
        #     t.z_dp("sarab", "sarasarabcabcsarabsarddamahmsarabsarabssarabywqosar"),
        #     [1, 2, 3, 4,1,2,3,4,5],
        # )
        self.assertEqual(
            t.z_dp("sarab", "sarasarab"),
            [1, 2, 3, 4, 1, 2, 3, 4, 5],
        )
        # self.assertEqual(
        #     t.z_dp("sarab", "saras"),
        #     [1, 2, 3, 4, 1],
        # )


if __name__ == "__main__":
    unittest.main()
