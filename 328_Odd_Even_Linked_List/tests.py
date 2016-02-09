#!/usr/bin/python3
from unittest import TestCase, main
from sol2 import NumArray


class Test(TestCase):
    sol = None

    def test0(self):
        self.sol = NumArray([1])
        ans = 1
        self.assertEqual(ans, self.sol.sumRange(0, 0))

    def test1(self):
        self.sol = NumArray([1, 2, 3])
        ans = 3
        self.assertEqual(ans, self.sol.sumRange(0, 1))

    def test2(self):
        self.sol = NumArray([1, 2, 3])
        ans = 5
        self.assertEqual(ans, self.sol.sumRange(1, 2))

    def test3(self):
        self.sol = NumArray([1, 2, 3])
        ans = 6
        self.assertEqual(ans, self.sol.sumRange(0, 2))

        # def test4(self):
        #     secret = "1234"
        #     guess = "2134"
        #     ans = "2A2B"
        #     self.assertEqual(ans, self.sol.getHint(secret, guess))
        #
        # def test5(self):
        #     secret = "1234"
        #     guess = "4321"
        #     ans = "0A4B"
        #     self.assertEqual(ans, self.sol.getHint(secret, guess))
        #
        # def test6(self):
        #     secret = ""
        #     guess = ""
        #     ans = "0A0B"
        #     self.assertEqual(ans, self.sol.getHint(secret, guess))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
