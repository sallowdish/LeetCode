#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

def split(n):
        l = []
        for i in n:
            l.append(list(i))
        return l

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = [0]
        self.assertEqual(self.sol.plusOne(n) ,[1])

    # overflow
    def test1(self):
        n = [9]
        self.assertEqual(self.sol.plusOne(n) ,[1,0])

    # long overflow
    def test2(self):
        n = [9,9,9]
        self.assertEqual(self.sol.plusOne(n), [1,0,0,0])

    # dissolved overflow
    def test3(self):
        n = [9,8,9]
        self.assertEqual(self.sol.plusOne(n), [9,9,0])

    # def test4(self):
    #     n = "    aVb "
    #     self.assertEqual(self.sol.plusOne(n) ,3)
    #
    # def test5(self):
    #     n = "    ab  IUHB POQPEQJ83894e2"
    #     self.assertEqual(self.sol.plusOne(n) ,len("POQPEQJ83894e2"))





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
