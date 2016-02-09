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
        n = split([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
        self.assertEqual(self.sol.isValidSudoku(n) ,True)

    def test1(self):
        n = split([".87654321","28.......","3........","4........","5........","6........","7........","8........","9........"])
        self.assertEqual(self.sol.isValidSudoku(n) ,False)

    def test2(self):
        n = split([".87654321","2........","3.....3..","4........","5........","6........","7........","8........","9........"])
        self.assertEqual(self.sol.isValidSudoku(n) ,False)

    def test3(self):
        n = split([".87654321","2........","3.7......","4........","5........","6........","7........","8........","9........"])
        self.assertEqual(self.sol.isValidSudoku(n) ,False)
    #
    # def test4(self):
    #     n = 5
    #     self.assertEqual(self.sol.isValidSudoku(n) ,self.ans[n - 1])




if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
