import unittest
from dataclasses import dataclass


@dataclass
class Pali:
    size: int
    index: int


def outerCharsAreEqual(s: str) -> bool:
    return s[0] == s[len(s) - 1]


# search from inside to outside
def searchRecursForLongerPalindrome(i: int, palSize: int, s: str) -> Pali:
    if i < 1 or i + palSize >= len(s):
        return Pali(palSize, i)
    if outerCharsAreEqual(s[i - 1 : i + palSize + 1]):
        return searchRecursForLongerPalindrome(i - 1, palSize + 2, s)
    return Pali(palSize, i)


def longestPalForCategory(s: str, blockSize: int) -> Pali:
    blocks = []
    for i in range(len(s) - blockSize + 1):
        sub = s[i : i + blockSize]
        if outerCharsAreEqual(sub):
            blocks.append(i)
    pali = Pali(1, 0)
    for i in blocks:
        newPali = searchRecursForLongerPalindrome(i, blockSize, s)
        if newPali.size > pali.size:
            pali = newPali
    return pali


class Solution:
    def longestPalindrome(self, s: str) -> str:
        evenPali = longestPalForCategory(s, 2)
        oddPali = longestPalForCategory(s, 3)
        if evenPali.size > oddPali.size:
            return s[evenPali.index : evenPali.index + evenPali.size]
        return s[oddPali.index : oddPali.index + oddPali.size]


class Test(unittest.TestCase):
    def test(self):
        t = Solution()
        self.assertEqual(t.longestPalindrome("aba"), "aba")
        self.assertEqual(t.longestPalindrome("cabac"), "cabac")
        self.assertEqual(t.longestPalindrome("abba"), "abba")
        self.assertEqual(t.longestPalindrome("cabba"), "abba")
        self.assertEqual(t.longestPalindrome("abbac"), "abba")
        self.assertEqual(t.longestPalindrome("abbbbackslfa"), "abbbba")
        self.assertEqual(t.longestPalindrome("cabafdqa"), "aba")
        self.assertEqual(t.longestPalindrome("cdabadfzqa"), "dabad")
        self.assertEqual(
            t.longestPalindrome("babaddtattarrattatddetartrateedredividerb"),
            "ddtattarrattatdd",
        )
        self.assertEqual(
            t.longestPalindrome(
                "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
            ),
            "qahaq",
        )


if __name__ == "__main__":
    unittest.main()
