#!/usr/bin/python3
from unittest import TestCase, main
from sol2 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    # whole test
    def test0_0(self):
        n = 2
        ans = [0, 1, 3, 2]
        ret = self.sol.grayCode(n)
        self.assertEqual(ans, ret)

    def test0_1(self):
        n = 3
        ans = [0, 1, 3, 2, 6, 7, 5, 4]
        ret = self.sol.grayCode(n)
        self.assertEqual(ans, ret)

    def test0_2(self):
        n = 4
        ans = [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
        ret = self.sol.grayCode(n)
        self.assertEqual(ans, ret)

        # real cases


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
