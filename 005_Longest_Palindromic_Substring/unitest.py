from tests import TestCase
from sol5 import Solution

class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s = ""
        self.assertEqual(self.sol.longestPalindrome(s), "")

    def test2(self):
        s = "a"
        self.assertEqual(self.sol.longestPalindrome(s), "a")

    def test3(self):
        s = "aa"
        self.assertEqual(self.sol.longestPalindrome(s), "aa")

    def test4(self):
        s = "ab"
        self.assertTrue(self.sol.longestPalindrome(s) in {"a", "b"})

    def test5(self):
        s = "abba"
        self.assertEqual(self.sol.longestPalindrome(s), "abba")

    def test6(self):
        s = "aaaa"
        self.assertEqual(self.sol.longestPalindrome(s), "aaaa")

    def test7(self):
        s = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
        self.assertEqual(self.sol.longestPalindrome(s),"qahaq")

    def test8(self):
        s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
        self.assertEqual(self.sol.longestPalindrome(s), s)

    def test9(self):
        s ="fdabbac"
        self.assertEqual(self.sol.longestPalindrome(s), "abba")
