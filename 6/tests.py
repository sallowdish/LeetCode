from unittest import TestCase
from sol2 import Solution

class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s = "PAYPALISHIRING"
        self.assertEqual(self.sol.convert(s, 3), "PAHNAPLSIIGYIR")

    def test2(self):
        s = "PAYPALISHIRING"
        self.assertEqual(self.sol.convert(s, 4), "PINALSIGYAHRPI")

    def test3(self):
        s = ""
        self.assertEqual(self.sol.convert(s, 1), "")

    def test4(self):
        s = "a"
        self.assertEqual(self.sol.convert(s, 1), "a")

    def test5(self):
        s = "abfewfeqrfq"
        self.assertEqual(self.sol.convert(s, 1), s)

    def test6(self):
        s = "ABCD"
        self.assertEqual(self.sol.convert(s, 2), "ACBD")

    def test7(self):
        s = "ABCDE"
        self.assertEqual(self.sol.convert(s, 4), "ABCED")

    def test8(self):
        s = "PAYPALISHIRING"
        self.assertEqual(self.sol.convert(s, 5), "PHASIYIRPLIGAN")

    def test9(self):
        s = "zcdffagygmalkzfmqavtzeqfjtmdxvvwxbefdmfjyfukhcwxctqdziliexlbtjzsmfxprfzqmvctxbqcuifurqcvqqyjzxbnfbcwidouzrowsgyopgiiyndoddxeabrhevgmzuiynywhfxywdggbvlsaopgqszyyvekuavuqtqxanxysgewbpocdfkwakuyfalbagvqblqcbnavvhrxyhbeplapvwncwydwgypimhmnwmksvcpulsyadapbwfdsdjqmhfutmgilutdqxumimmlrmauifyalhqxqytmmzuxtpalouzxilkaxkufsuhfdacwyvikwekrukfihehpqtrpeoxyiedoehkeesrcybtunyfudmmvgfkmthmcorsuaczewsiutbpgcudhircqwoeqyqumjogjqhpozxiubzddvikezowxebpctlqdzzmrgcfibqecrhhnrtrshnsoqhqkvhnwizoqdvahnflhotugmnawcsktccdxlstttjkxhkgwrrdgkzozmoxphjkllpizhduapgzwrfukzaslzgkoxjfgsprgezflezntgnrzumltoefnkpdhbiptzgzdhgqmighqtzpnnchbgmqrduaeesaeybjiiawqgdgbcxorzxuillbrhdxlvxpwzbejdazlfhmkgcbhcwpnjqequcdrbvncwrlztmkzvyjbaklciaqrtwhpangeiugensdhgpgcnrfnbqsktkdogndjalniftmvnrcuikyvbdkeueqnoubxhgghrvrzofueyyagiydlbpp"
        self.assertEqual(self.sol.convert(s,789), "zcdffagygmalkzfmqavtzeqfjtmdxvvwxbefdmfjyfukhcwxctqdziliexlbtjzsmfxprfzqmvctxbqcuifurqcvqqyjzxbnfbcwidouzrowsgyopgiiyndoddxeabrhevgmzuiynywhfxywdggbvlsaopgqszyyvekuavuqtqxanxysgewbpocdfkwakuyfalbagvqblqcbnavvhrxyhbeplapvwncwydwgypimhmnwmksvcpulsyadapbwfdsdjqmhfutmgilutdqxumimmlrmauifyalhqxqytmmzuxtpalouzxilkaxkufsuhfdacwyvikwekrukfihehpqtrpeoxyiedoehkeesrcybtunyfudmmvgfkmthmcorsuaczewsiutbpgcudhircqwoeqyqumjogjqhpozxiubzddvikezowxebpctlqdzzmrgcfibqecrhhnrtrshnsoqhqkvhnwizoqdvahnflhotugmnawcsktccdxlstttjkxhkgwrrdgkzozmoxphjkllpizhduapgzwrfukzaslzgkoxjfgsprgezflezntgnrzumltoefnkpdhbiptzgzdhgqmighqtzpnnchbgmqrduaeesaeybjiiawqgdgbcxorzxuillbrhdxlvxpwzbejdazlfhmkgcbhcwpnjqequcdrbvncwrlztmkzvyjbaklciaqrtwhpangeiugensdhgpgcnrfnbqsktkdogndjalniftmvnrcuikyvbdkeueqnoubxhgghrvrzofueyyapgpibyld")