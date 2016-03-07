#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = "/"
        ans = "/"
        self.assertEqual(self.sol.simplifyPath(n), ans)

    def test1(self):
        n = "/home/"
        ans = "/home"
        self.assertEqual(self.sol.simplifyPath(n), ans)

    def test2(self):
        n = "/a/./b/../../c/"
        ans = "/c"
        self.assertEqual(self.sol.simplifyPath(n), ans)

    def test3(self):
        n = "/../"
        ans = "/"
        self.assertEqual(self.sol.simplifyPath(n), ans)

    def test4(self):
        n = "/home//foo/"
        ans = "/home/foo"
        self.assertEqual(self.sol.simplifyPath(n), ans)
        #
        # def test5(self):
        #     n = "    ab  IUHB POQPEQJ83894e2"
        #     self.assertEqual(self.sol.simplifyPath(n) ,len("POQPEQJ83894e2"))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
