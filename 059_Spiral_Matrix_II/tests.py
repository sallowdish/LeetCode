#!/usr/bin/python3
from unittest import TestCase
from collections import Counter
from sol1 import Solution
import logging, unittest


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        m = 4
        n = 5
        step = (0, 0, 'right')
        steps = [step]
        for i in range(m * n - 1):
            step = self.sol.get_next_step(step[0], step[1], step[2], m, n)
            steps += [step]
        ans = [(0, 0, 'right'), (0, 1, 'right'), (0, 2, 'right'), (0, 3,
                                                                   'right'),
               (0, 4, 'down'), (1, 4, 'down'), (2, 4, 'down'), (3, 4, 'left'),
               (3, 3, 'left'), (3, 2, 'left'), (3, 1, 'left'), (3, 0, 'up'),
               (2, 0, 'up'), (1, 0, 'right'), (1, 1, 'right'), (1, 2, 'right'),
               (1, 3, 'down'), (2, 3, 'left'), (2, 2, 'left'), (2, 1, 'up')]
        self.assertEqual(ans, steps)

    def test1(self):
        n = 0
        ans = [[]]
        self.assertEqual(ans, self.sol.generateMatrix(n))

    def test2(self):
        n = 1
        ans = [[1]]
        self.assertEqual(ans, self.sol.generateMatrix(n))

    def test3(self):
        n = 2
        ans = [[1, 2], [4, 3]]
        self.assertEqual(ans, self.sol.generateMatrix(n))

    def test4(self):
        n = 3
        ans = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(ans, self.sol.generateMatrix(n))

        # def test5(self):
        #     n = [[3], [2]]
        #     ans = [3, 2]
        #     self.assertEqual(ans, self.sol.generateMatrix(n))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
