#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = [1, 2, 3]
        ans = [1, 2, 3]
        self.assertEqual(ans, self.sol.moveZeroes(n))

    def test1(self):
        n = [1, 2, 0, 3]
        ans = [1, 2, 3, 0]
        self.assertEqual(ans, self.sol.moveZeroes(n))

    def test2(self):
        n = [1, 2, 3, 0, 0, 0, 5]
        ans = [1, 2, 3, 5, 0, 0, 0]
        self.assertEqual(ans, self.sol.moveZeroes(n))

    def test3(self):
        n = [1, 2, 0, 3, 0, 4]
        ans = [1, 2, 3, 4, 0, 0]
        self.assertEqual(ans, self.sol.moveZeroes(n))

    def test4(self):
        n = [0, 0, 0, 0]
        ans = [0, 0, 0, 0]
        self.assertEqual(ans, self.sol.moveZeroes(n))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
