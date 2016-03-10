#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = [[]]
        ans = [[]]
        self.assertEqual(self.sol.setZeroes(n), ans)

    def test1(self):
        n = [[1]]
        ans = [[1]]
        self.assertEqual(self.sol.setZeroes(n), ans)

    def test2(self):
        n = [[1, 0]]
        ans = [[0, 0]]
        self.assertEqual(self.sol.setZeroes(n), ans)

    def test3(self):
        n = [[1, 1], [0, 1]]
        ans = [[0, 1], [0, 0]]
        self.assertEqual(self.sol.setZeroes(n), ans)

    def test4(self):
        n = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3],
             [0, 0, 1, 1]]
        ans = [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 3],
               [0, 0, 0, 0]]
        self.assertEqual(self.sol.setZeroes(n), ans)
        #
        # def test5(self):
        #     n = "    ab  IUHB POQPEQJ83894e2"
        #     self.assertEqual(self.sol.setZeroes(n) ,len("POQPEQJ83894e2"))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
