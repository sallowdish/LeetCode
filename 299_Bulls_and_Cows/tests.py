#!/usr/bin/python3
from unittest import TestCase, main
from sol2 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        secret = "1807"
        guess = "7810"
        ans = "1A3B"
        self.assertEqual(ans, self.sol.getHint(secret, guess))

    def test1(self):
        secret = "1123"
        guess = "0111"
        ans = "1A1B"
        self.assertEqual(ans, self.sol.getHint(secret, guess))

    def test2(self):
        secret = "0000"
        guess = "1111"
        ans = "0A0B"
        self.assertEqual(ans, self.sol.getHint(secret, guess))

    def test3(self):
        secret = "1111"
        guess = "1111"
        ans = "4A0B"
        self.assertEqual(ans, self.sol.getHint(secret, guess))

    def test4(self):
        secret = "1234"
        guess = "2134"
        ans = "2A2B"
        self.assertEqual(ans, self.sol.getHint(secret, guess))

    def test5(self):
        secret = "1234"
        guess = "4321"
        ans = "0A4B"
        self.assertEqual(ans, self.sol.getHint(secret, guess))

    def test6(self):
        secret = ""
        guess = ""
        ans = "0A0B"
        self.assertEqual(ans, self.sol.getHint(secret, guess))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
