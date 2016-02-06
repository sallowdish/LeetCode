#!/usr/bin/python3
from unittest import TestCase, main
from sol2 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    # test is_over_lap
    # def test0_0(self):
    #     n = []
    #     m = 0
    #     ans = True
    #     self.assertEqual(ans, bool(self.sol.is_over_lap(((-3, 0), (3, 4)), ((0, -1), (9, 2)))))
    #
    # def test0_1(self):
    #     n = [1]
    #     m = 2
    #     ans = False
    #     self.assertEqual(ans, bool(self.sol.is_over_lap(((-5, -5), (0, 0)), ((1, 1), (3, 3)))))
    #
    # # rec_2 in rec_1
    # def test0_2(self):
    #     n = [1]
    #     m = 2
    #     ans = True
    #     self.assertEqual(ans, bool(self.sol.is_over_lap(((-5, -5), (5, 5)), ((0, 0), (3, 3)))))
    #
    # # 2 points of rec_2 in rec_1
    # def test0_3(self):
    #     n = [1]
    #     m = 2
    #     ans = True
    #     self.assertEqual(ans, bool(self.sol.is_over_lap(((-5, -5), (5, 5)), ((0, 0), (10, 3)))))

    ## functional test
    def test1_0(self):
        n = []
        m = 0
        ans = True
        self.assertEqual(6, self.sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))

    def test1_1(self):
        n = []
        m = 0
        ans = 9
        self.assertEqual(ans, self.sol.computeArea(-5, -5, 5, 5, 0, 0, 3, 3))

    def test1_2(self):
        n = []
        m = 0
        ans = 15
        self.assertEqual(ans, self.sol.computeArea(-5, -5, 5, 5, 0, 0, 10, 3))

    def test1_3(self):
        n = []
        m = 0
        ans = 20
        self.assertEqual(ans, self.sol.computeArea(-5, -5, 5, 5, 0, -6, 2, 6))



if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
