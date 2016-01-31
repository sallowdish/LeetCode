#!/usr/bin/python3
from unittest import TestCase, main
from sol3 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 0
        ans = 0
        self.assertEqual(ans, self.sol.countPrimes(n))

    def test1(self):
        n = 1
        ans = 0
        self.assertEqual(ans, self.sol.countPrimes(n))

    def test2_1(self):
        n = 2
        ans = 0
        self.assertEqual(ans, self.sol.countPrimes(n))

    def test2_2(self):
        n = 3
        ans = 1
        self.assertEqual(ans, self.sol.countPrimes(n))

    def test3(self):
        n = 5
        ans = 2
        self.assertEqual(ans, self.sol.countPrimes(n))

    def test4(self):
        n = 50
        ans = 15
        self.assertEqual(ans, self.sol.countPrimes(n))

    def test5(self):
        n = 499979
        ans = 41537
        self.assertEqual(ans, self.sol.countPrimes(n))

    # def test6(self):
    #     n = 8
    #     ans = 35
    #     self.assertEqual(self.sol.countPrimes(n), ans)


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
