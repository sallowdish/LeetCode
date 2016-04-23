#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    # whole test
    def test0_0(self):
        n = ""
        ans = 0
        self.run_test(n, ans)

    def test0_1(self):
        n = "0"
        ans = 0
        self.run_test(n, ans)

    def test0_2(self):
        n = "4352421"
        ans = 4
        self.run_test(n, ans)

    def test1_0(self):
        n = "11"
        ans = 2
        self.run_test(n, ans)

    def test1_1(self):
        n = "100"
        ans = 0
        self.run_test(n, ans)

    def test1_2(self):
        n = "101"
        ans = 1
        self.run_test(n, ans)

    def test1_3(self):
        n = "110"
        ans = 1
        self.run_test(n, ans)

    def test1_4(self):
        n = "230"
        ans = 0
        self.run_test(n, ans)

    def run_test(self, n, ans):
        ret = self.sol.numDecodings(n)
        self.assertEqual(ans, ret)


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
