#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 9
        ans = 3
        self.assertEqual(self.sol.mySqrt(n), ans)

    # overflow
    def test1(self):
        n = 1
        ans = 1
        self.assertEqual(self.sol.mySqrt(n), ans)

    # long overflow
    def test2(self):
        n = 8
        ans = 2
        self.assertEqual(self.sol.mySqrt(n), ans)

    # dissolved overflow
    def test3(self):
        n = 625
        ans = 25
        self.assertEqual(self.sol.mySqrt(n), ans)

        # def test4(self):
        #     n = "    aVb "
        #     self.assertEqual(self.sol.mySqrt(n) ,3)
        #
        # def test5(self):
        #     n = "    ab  IUHB POQPEQJ83894e2"
        #     self.assertEqual(self.sol.mySqrt(n) ,len("POQPEQJ83894e2"))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
