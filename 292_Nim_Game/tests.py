#!/usr/bin/python3
from unittest import TestCase, main
from sol2 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 1
        ans = True
        self.assertEqual(ans, self.sol.canWinNim(n))

    def test1(self):
        n = 4
        ans = False
        self.assertEqual(ans, self.sol.canWinNim(n))

    def test2(self):
        n = 5
        ans = True
        self.assertEqual(ans, self.sol.canWinNim(n))

    def test3(self):
        n = 10
        ans = True
        self.assertEqual(ans, self.sol.canWinNim(n))

    def test6(self):
        n = 12
        ans = False
        self.assertEqual(ans, self.sol.canWinNim(n))

    def test4(self):
        n = 100
        ans = False
        self.assertEqual(ans, self.sol.canWinNim(n))

        # def test5(self):
        #     n = 1348820612
        #     ans = True
        #     self.assertEqual(ans, self.sol.canWinNim(n))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
