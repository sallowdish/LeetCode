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
        l1 = []
        l2 = []
        self.assertEqual(self.sol.merge(l1, len(l1), l2, len(l2)) ,[])

    # overflow
    def test1(self):
        l1 = [1,5,9]
        l2 = []
        self.assertEqual(self.sol.merge(l1, len(l1), l2, len(l2)) ,[1,5,9])

    # long overflow
    def test2(self):
        l1 = []
        l2 = [1,5,9]
        self.assertEqual(self.sol.merge(l1, len(l1), l2, len(l2)), [1,5,9])

    # dissolved overflow
    def test3(self):
        l1 = [1,5,9]
        l2 = [2,6,10]
        self.assertEqual(self.sol.merge(l1, len(l1), l2, len(l2)), [1,2,5,6,9,10])

    def test4(self):
        l1 = [1,5,9]
        l2 = [-15, -10, -5, 0 , 1]
        self.assertEqual(self.sol.merge(l1, len(l1), l2, len(l2)) ,[-15,-10,-5,0,1,1,5,9])

    def test5(self):
        l1 = [1, 99]
        l2 = [-1, 2,3,4,100]
        self.assertEqual(self.sol.merge(l1, len(l1), l2, len(l2)) ,[-1,1,2,3,4,99,100])

    def test6(self):
        l1 = [0]
        l2 = [1]
        self.assertEqual(self.sol.merge(l1, 0, l2, 1) ,[1])



if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
