#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 1
        k = 0
        self.assertEqual(True, self.sol.isHappy(n))

    def test1(self):
        n = 19
        k = 0
        self.assertEqual(True, self.sol.isHappy(n))

    def test2_1(self):
        n = 4
        k = 1
        self.assertEqual(False, self.sol.isHappy(n))

    def test2_2(self):
        n = 14
        ans = False
        self.assertEqual(ans, self.sol.isHappy(n))
    #
    # def test3(self):
    #     n = [2,1,1,2]
    #     k = 4
    #     self.assertEqual(self.sol.isHappy(n), 4)
    #
    # def test4(self):
    #     n = [155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]
    #     k = 4
    #     self.assertEqual(self.sol.isHappy(n), 4517)

    # def test5(self):
    #     n = [1,2,3,4]
    #     k = -1
    #     self.assertEqual(self.sol.isHappy(n), [4,1,2,3])

    # def test6(self):
    #     n = 8
    #     k = 35
    #     self.assertEqual(self.sol.isHappy(n), ans)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
