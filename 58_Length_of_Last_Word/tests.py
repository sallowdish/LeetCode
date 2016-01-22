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
        n = ""
        self.assertEqual(self.sol.lengthOfLastWord(n) ,0)

    def test1(self):
        n = "    "
        self.assertEqual(self.sol.lengthOfLastWord(n) ,0)

    def test2(self):
        n = "   a"
        self.assertEqual(self.sol.lengthOfLastWord(n) ,1)

    def test3(self):
        n = "    ab"
        self.assertEqual(self.sol.lengthOfLastWord(n) ,2)

    def test4(self):
        n = "    aVb "
        self.assertEqual(self.sol.lengthOfLastWord(n) ,3)

    def test5(self):
        n = "    ab  IUHB POQPEQJ83894e2"
        self.assertEqual(self.sol.lengthOfLastWord(n) ,len("POQPEQJ83894e2"))





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
