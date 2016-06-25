#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = ""
        m = ""
        ans = ""
        self.assertEqual(self.sol.addBinary(n, m), ans)

    # overflow
    def test1(self):
        n = "1"
        m = "0"
        ans = "1"
        self.assertEqual(self.sol.addBinary(n, m), ans)

    # long overflow
    def test2(self):
        n = "1"
        m = "1"
        ans = "10"
        self.assertEqual(self.sol.addBinary(n, m), ans)

    # dissolved overflow
    def test3(self):
        n = "11"
        m = "1"
        ans = "100"
        self.assertEqual(self.sol.addBinary(n, m), ans)

        # def test4(self):
        #     n = "    aVb "
        #     self.assertEqual(self.sol.addBinary(n, m) ,3)
        #
        # def test5(self):
        #     n = "    ab  IUHB POQPEQJ83894e2"
        #     self.assertEqual(self.sol.addBinary(n, m) ,len("POQPEQJ83894e2"))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
