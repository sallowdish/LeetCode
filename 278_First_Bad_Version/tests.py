#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 1
        ans = None
        self.assertEqual(ans, self.sol.firstBadVersion(n))

    def test1(self):
        n = 5
        ans = 5
        self.assertEqual(ans, self.sol.firstBadVersion(n))

    def test2(self):
        n = 10
        ans = 5
        self.assertEqual(ans, self.sol.firstBadVersion(n))

    def test3(self):
        n = 15
        ans = 5
        self.assertEqual(ans, self.sol.firstBadVersion(n))

    def test4(self):
        n = 100
        ans = 5
        self.assertEqual(ans, self.sol.firstBadVersion(n))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
