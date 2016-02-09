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
        n = 0
        self.assertEqual(self.sol.climbStairs(n) ,0)

    # overflow
    def test1(self):
        n = 1
        self.assertEqual(self.sol.climbStairs(n) ,1)

    # long overflow
    def test2(self):
        n = 2
        self.assertEqual(self.sol.climbStairs(n), 2)

    # dissolved overflow
    def test3(self):
        n = 3
        self.assertEqual(self.sol.climbStairs(n), 3)

    def test4(self):
        n = 7
        self.assertEqual(self.sol.climbStairs(n) ,21)

    def test5(self):
        n = 100
        phi = (5**0.5+1)/2
        self.assertEqual(self.sol.climbStairs(n) ,int((phi**(n+2))/(phi+2)))





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
