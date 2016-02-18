#!/usr/bin/python3
from unittest import TestCase
from collections import Counter
from sol2 import Solution
import logging, unittest


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = ""
        m = ""
        ans = "0"
        self.assertEqual(ans, self.sol.multiply(n, m))

    def test1(self):
        n = "000"
        m = "00"
        ans = "0"
        self.assertEqual(ans, self.sol.multiply(n, m))

    def test2(self):
        n = "123"
        m = "321"
        ans = "39483"
        self.assertEqual(ans, self.sol.multiply(n, m))

    def test3(self):
        m = "4133241"
        n = "01234"
        ans = "5100419394"
        self.assertEqual(ans, self.sol.multiply(n, m))

    def test4(self):
        n = "887215951631860898850672165670178191617772888069065122540029356168329298406"
        m= "44311453195435793851382571199824255312824367056642992271581465800553855214"
        ans = "39313828114979231346741890629908862134626208999146274773519636237148727290076339806887956594176739431973330476821567938426157332813975758391124988884"
        self.assertEqual(ans, self.sol.multiply(n, m))
    #
    # def test5(self):
    #     n = [1, 3, 5, 6]
    #     m = 5
    #     ans = 2
    #     self.assertEqual(ans, self.sol.multiply(n, m))
    #
    # def test6(self):
    #     n = [1, 3, 5, 6]
    #     m = 2
    #     ans = 1
    #     self.assertEqual(ans, self.sol.multiply(n, m))
    #
    # def test7(self):
    #     n = [1, 3, 5, 6]
    #     m = 0
    #     ans = 0
    #     self.assertEqual(ans, self.sol.multiply(n, m))
    #
    # def test8(self):
    #     n = [1, 3]
    #     m = 1
    #     ans = 0
    #     self.assertEqual(ans, self.sol.multiply(n, m))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
