#!/usr/bin/python3
from unittest import TestCase, main
from sol2 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 0
        k = 0
        self.assertEqual(self.sol.reverseBits(n), 0)

    def test1(self):
        n = 1
        k = 0
        self.assertEqual(self.sol.reverseBits(n), 2147483648)

    def test2_1(self):
        n = 43261596
        k = 1
        self.assertEqual(self.sol.reverseBits(n), 964176192)

    def test2_2(self):
        n = 4294967295
        k = 2
        self.assertEqual(self.sol.reverseBits(n), n)

    # def test3(self):
    #     n = [1,2,3,4,5,6,7]
    #     k = 4
    #     self.assertEqual(self.sol.reverseBits(n), [5,6,7,1,2,3,4])
    #
    # def test4(self):
    #     n = [1,2,3]
    #     k = 4
    #     self.assertEqual(self.sol.reverseBits(n), [2,3,1])

    # def test5(self):
    #     n = [1,2,3,4]
    #     k = -1
    #     self.assertEqual(self.sol.reverseBits(n), [4,1,2,3])

    # def test6(self):
    #     n = 8
    #     k = 35
    #     self.assertEqual(self.sol.reverseBits(n), ans)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
