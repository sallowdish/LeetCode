#!/usr/bin/python3
from unittest import TestCase
from collections import Counter
from sol3 import Solution
import logging, unittest


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = [[1]]
        ans = [[1]]
        self.assertEqual(ans, self.sol.rotate(n))

    def test1(self):
        n = [[1, 2], [3, 4]]
        ans = [[3, 1], [4, 2]]
        self.assertEqual(ans, self.sol.rotate(n))

    def test2(self):
        n = [[3, 1], [4, 2]]
        ans = [[4, 3], [2, 1]]
        self.assertEqual(ans, self.sol.rotate(n))

    def test3(self):
        n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ans = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(ans, self.sol.rotate(n))

        # def test4(self):
        #     n = [3, 3, 0, 0, 2, 3, 2]
        #     ans = [[0, 0, 2, 2, 3, 3, 3], [0, 0, 2, 3, 2, 3, 3], [0, 0, 2, 3, 3, 2, 3], [0, 0, 2, 3, 3, 3, 2],
        #            [0, 0, 3, 2, 2, 3, 3], [0, 0, 3, 2, 3, 2, 3], [0, 0, 3, 2, 3, 3, 2], [0, 0, 3, 3, 2, 2, 3],
        #            [0, 0, 3, 3, 2, 3, 2], [0, 0, 3, 3, 3, 2, 2], [0, 2, 0, 2, 3, 3, 3], [0, 2, 0, 3, 2, 3, 3],
        #            [0, 2, 0, 3, 3, 2, 3], [0, 2, 0, 3, 3, 3, 2], [0, 2, 2, 0, 3, 3, 3], [0, 2, 2, 3, 0, 3, 3],
        #            [0, 2, 2, 3, 3, 0, 3], [0, 2, 2, 3, 3, 3, 0], [0, 2, 3, 0, 2, 3, 3], [0, 2, 3, 0, 3, 2, 3],
        #            [0, 2, 3, 0, 3, 3, 2], [0, 2, 3, 2, 0, 3, 3], [0, 2, 3, 2, 3, 0, 3], [0, 2, 3, 2, 3, 3, 0],
        #            [0, 2, 3, 3, 0, 2, 3], [0, 2, 3, 3, 0, 3, 2], [0, 2, 3, 3, 2, 0, 3], [0, 2, 3, 3, 2, 3, 0],
        #            [0, 2, 3, 3, 3, 0, 2], [0, 2, 3, 3, 3, 2, 0], [0, 3, 0, 2, 2, 3, 3], [0, 3, 0, 2, 3, 2, 3],
        #            [0, 3, 0, 2, 3, 3, 2], [0, 3, 0, 3, 2, 2, 3], [0, 3, 0, 3, 2, 3, 2], [0, 3, 0, 3, 3, 2, 2],
        #            [0, 3, 2, 0, 2, 3, 3], [0, 3, 2, 0, 3, 2, 3], [0, 3, 2, 0, 3, 3, 2], [0, 3, 2, 2, 0, 3, 3],
        #            [0, 3, 2, 2, 3, 0, 3], [0, 3, 2, 2, 3, 3, 0], [0, 3, 2, 3, 0, 2, 3], [0, 3, 2, 3, 0, 3, 2],
        #            [0, 3, 2, 3, 2, 0, 3], [0, 3, 2, 3, 2, 3, 0], [0, 3, 2, 3, 3, 0, 2], [0, 3, 2, 3, 3, 2, 0],
        #            [0, 3, 3, 0, 2, 2, 3], [0, 3, 3, 0, 2, 3, 2], [0, 3, 3, 0, 3, 2, 2], [0, 3, 3, 2, 0, 2, 3],
        #            [0, 3, 3, 2, 0, 3, 2], [0, 3, 3, 2, 2, 0, 3], [0, 3, 3, 2, 2, 3, 0], [0, 3, 3, 2, 3, 0, 2],
        #            [0, 3, 3, 2, 3, 2, 0], [0, 3, 3, 3, 0, 2, 2], [0, 3, 3, 3, 2, 0, 2], [0, 3, 3, 3, 2, 2, 0],
        #            [2, 0, 0, 2, 3, 3, 3], [2, 0, 0, 3, 2, 3, 3], [2, 0, 0, 3, 3, 2, 3], [2, 0, 0, 3, 3, 3, 2],
        #            [2, 0, 2, 0, 3, 3, 3], [2, 0, 2, 3, 0, 3, 3], [2, 0, 2, 3, 3, 0, 3], [2, 0, 2, 3, 3, 3, 0],
        #            [2, 0, 3, 0, 2, 3, 3], [2, 0, 3, 0, 3, 2, 3], [2, 0, 3, 0, 3, 3, 2], [2, 0, 3, 2, 0, 3, 3],
        #            [2, 0, 3, 2, 3, 0, 3], [2, 0, 3, 2, 3, 3, 0], [2, 0, 3, 3, 0, 2, 3], [2, 0, 3, 3, 0, 3, 2],
        #            [2, 0, 3, 3, 2, 0, 3], [2, 0, 3, 3, 2, 3, 0], [2, 0, 3, 3, 3, 0, 2], [2, 0, 3, 3, 3, 2, 0],
        #            [2, 2, 0, 0, 3, 3, 3], [2, 2, 0, 3, 0, 3, 3], [2, 2, 0, 3, 3, 0, 3], [2, 2, 0, 3, 3, 3, 0],
        #            [2, 2, 3, 0, 0, 3, 3], [2, 2, 3, 0, 3, 0, 3], [2, 2, 3, 0, 3, 3, 0], [2, 2, 3, 3, 0, 0, 3],
        #            [2, 2, 3, 3, 0, 3, 0], [2, 2, 3, 3, 3, 0, 0], [2, 3, 0, 0, 2, 3, 3], [2, 3, 0, 0, 3, 2, 3],
        #            [2, 3, 0, 0, 3, 3, 2], [2, 3, 0, 2, 0, 3, 3], [2, 3, 0, 2, 3, 0, 3], [2, 3, 0, 2, 3, 3, 0],
        #            [2, 3, 0, 3, 0, 2, 3], [2, 3, 0, 3, 0, 3, 2], [2, 3, 0, 3, 2, 0, 3], [2, 3, 0, 3, 2, 3, 0],
        #            [2, 3, 0, 3, 3, 0, 2], [2, 3, 0, 3, 3, 2, 0], [2, 3, 2, 0, 0, 3, 3], [2, 3, 2, 0, 3, 0, 3],
        #            [2, 3, 2, 0, 3, 3, 0], [2, 3, 2, 3, 0, 0, 3], [2, 3, 2, 3, 0, 3, 0], [2, 3, 2, 3, 3, 0, 0],
        #            [2, 3, 3, 0, 0, 2, 3], [2, 3, 3, 0, 0, 3, 2], [2, 3, 3, 0, 2, 0, 3], [2, 3, 3, 0, 2, 3, 0],
        #            [2, 3, 3, 0, 3, 0, 2], [2, 3, 3, 0, 3, 2, 0], [2, 3, 3, 2, 0, 0, 3], [2, 3, 3, 2, 0, 3, 0],
        #            [2, 3, 3, 2, 3, 0, 0], [2, 3, 3, 3, 0, 0, 2], [2, 3, 3, 3, 0, 2, 0], [2, 3, 3, 3, 2, 0, 0],
        #            [3, 0, 0, 2, 2, 3, 3], [3, 0, 0, 2, 3, 2, 3], [3, 0, 0, 2, 3, 3, 2], [3, 0, 0, 3, 2, 2, 3],
        #            [3, 0, 0, 3, 2, 3, 2], [3, 0, 0, 3, 3, 2, 2], [3, 0, 2, 0, 2, 3, 3], [3, 0, 2, 0, 3, 2, 3],
        #            [3, 0, 2, 0, 3, 3, 2], [3, 0, 2, 2, 0, 3, 3], [3, 0, 2, 2, 3, 0, 3], [3, 0, 2, 2, 3, 3, 0],
        #            [3, 0, 2, 3, 0, 2, 3], [3, 0, 2, 3, 0, 3, 2], [3, 0, 2, 3, 2, 0, 3], [3, 0, 2, 3, 2, 3, 0],
        #            [3, 0, 2, 3, 3, 0, 2], [3, 0, 2, 3, 3, 2, 0], [3, 0, 3, 0, 2, 2, 3], [3, 0, 3, 0, 2, 3, 2],
        #            [3, 0, 3, 0, 3, 2, 2], [3, 0, 3, 2, 0, 2, 3], [3, 0, 3, 2, 0, 3, 2], [3, 0, 3, 2, 2, 0, 3],
        #            [3, 0, 3, 2, 2, 3, 0], [3, 0, 3, 2, 3, 0, 2], [3, 0, 3, 2, 3, 2, 0], [3, 0, 3, 3, 0, 2, 2],
        #            [3, 0, 3, 3, 2, 0, 2], [3, 0, 3, 3, 2, 2, 0], [3, 2, 0, 0, 2, 3, 3], [3, 2, 0, 0, 3, 2, 3],
        #            [3, 2, 0, 0, 3, 3, 2], [3, 2, 0, 2, 0, 3, 3], [3, 2, 0, 2, 3, 0, 3], [3, 2, 0, 2, 3, 3, 0],
        #            [3, 2, 0, 3, 0, 2, 3], [3, 2, 0, 3, 0, 3, 2], [3, 2, 0, 3, 2, 0, 3], [3, 2, 0, 3, 2, 3, 0],
        #            [3, 2, 0, 3, 3, 0, 2], [3, 2, 0, 3, 3, 2, 0], [3, 2, 2, 0, 0, 3, 3], [3, 2, 2, 0, 3, 0, 3],
        #            [3, 2, 2, 0, 3, 3, 0], [3, 2, 2, 3, 0, 0, 3], [3, 2, 2, 3, 0, 3, 0], [3, 2, 2, 3, 3, 0, 0],
        #            [3, 2, 3, 0, 0, 2, 3], [3, 2, 3, 0, 0, 3, 2], [3, 2, 3, 0, 2, 0, 3], [3, 2, 3, 0, 2, 3, 0],
        #            [3, 2, 3, 0, 3, 0, 2], [3, 2, 3, 0, 3, 2, 0], [3, 2, 3, 2, 0, 0, 3], [3, 2, 3, 2, 0, 3, 0],
        #            [3, 2, 3, 2, 3, 0, 0], [3, 2, 3, 3, 0, 0, 2], [3, 2, 3, 3, 0, 2, 0], [3, 2, 3, 3, 2, 0, 0],
        #            [3, 3, 0, 0, 2, 2, 3], [3, 3, 0, 0, 2, 3, 2], [3, 3, 0, 0, 3, 2, 2], [3, 3, 0, 2, 0, 2, 3],
        #            [3, 3, 0, 2, 0, 3, 2], [3, 3, 0, 2, 2, 0, 3], [3, 3, 0, 2, 2, 3, 0], [3, 3, 0, 2, 3, 0, 2],
        #            [3, 3, 0, 2, 3, 2, 0], [3, 3, 0, 3, 0, 2, 2], [3, 3, 0, 3, 2, 0, 2], [3, 3, 0, 3, 2, 2, 0],
        #            [3, 3, 2, 0, 0, 2, 3], [3, 3, 2, 0, 0, 3, 2], [3, 3, 2, 0, 2, 0, 3], [3, 3, 2, 0, 2, 3, 0],
        #            [3, 3, 2, 0, 3, 0, 2], [3, 3, 2, 0, 3, 2, 0], [3, 3, 2, 2, 0, 0, 3], [3, 3, 2, 2, 0, 3, 0],
        #            [3, 3, 2, 2, 3, 0, 0], [3, 3, 2, 3, 0, 0, 2], [3, 3, 2, 3, 0, 2, 0], [3, 3, 2, 3, 2, 0, 0],
        #            [3, 3, 3, 0, 0, 2, 2], [3, 3, 3, 0, 2, 0, 2], [3, 3, 3, 0, 2, 2, 0], [3, 3, 3, 2, 0, 0, 2],
        #            [3, 3, 3, 2, 0, 2, 0], [3, 3, 3, 2, 2, 0, 0]]
        #     self.assertEqual(ans, self.sol.rotate(n))
        #     #
        #     # def test5(self):
        #     #     n = [1, 3, 5, 6]
        #     #
        #     #     ans = 2
        #     #     self.assertEqual(ans, self.sol.rotate(n))
        #     #
        #     # def test6(self):
        #     #     n = [1, 3, 5, 6]
        #     #
        #     #     ans = 1
        #     #     self.assertEqual(ans, self.sol.rotate(n))
        #     #
        #     # def test7(self):
        #     #     n = [1, 3, 5, 6]
        #     #
        #     #     ans = 0
        #     #     self.assertEqual(ans, self.sol.rotate(n))
        #     #
        #     # def test8(self):
        #     #     n = [1, 3]
        #     #
        #     #     ans = 0
        #     #     self.assertEqual(ans, self.sol.rotate(n))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
