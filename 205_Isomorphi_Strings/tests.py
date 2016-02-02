#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):

    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = ""
        m = ""
        ans = True
        self.assertEqual(ans, self.sol.isIsomorphic(n, m))

    def test1(self):
        n = "a"
        m = "b"
        ans = True
        self.assertEqual(ans, self.sol.isIsomorphic(n, m))

    def test2_1(self):
        n = "aa"
        m = "ab"
        ans = False
        self.assertEqual(ans, self.sol.isIsomorphic(n, m))

    def test2_2(self):
        n = "egg"
        m = "add"
        ans = True
        self.assertEqual(ans, self.sol.isIsomorphic(n, m))

    def test3(self):
        n = "paper"
        m = "title"
        ans = True
        self.assertEqual(ans, self.sol.isIsomorphic(n, m))

    def test4(self):
        n = "foo"
        m = "bar"
        ans = False
        self.assertEqual(ans, self.sol.isIsomorphic(n, m))

    # def test5(self):
    #     n = [1,2,3,4]
    #     ans = -1
    #     self.assertEqual(ans, self.sol.isIsomorphic(n, m))

    # def test6(self):
    #     n = 8
    #     ans = 35
    #     self.assertEqual(ans, self.sol.isIsomorphic(n, m), ans)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
