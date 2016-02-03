#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = []
        m = 0
        ans = False
        self.assertEqual(ans, self.sol.containsNearbyDuplicate(n, m))

    def test1(self):
        n = [1]
        m = 2
        ans = False
        self.assertEqual(ans, self.sol.containsNearbyDuplicate(n, m))

    def test2_1(self):
        n = [1, 2]
        m = 2
        ans = False
        self.assertEqual(ans, self.sol.containsNearbyDuplicate(n, m))

    def test2_2(self):
        n = [1, 2, 1]
        m = 2
        ans = True
        self.assertEqual(ans, self.sol.containsNearbyDuplicate(n, m))

    def test3(self):
        n = [1, 2, 1]
        m = 1
        ans = False
        self.assertEqual(ans, self.sol.containsNearbyDuplicate(n, m))

    def test4(self):
        n = [1, 2, 3, 1, 4, 5, 1]
        m = 6
        ans = True
        self.assertEqual(ans, self.sol.containsNearbyDuplicate(n, m))

        # def test5(self):
        #     n = [1,2,3,4]
        #     ans = -1
        #     self.assertEqual(ans, self.sol.containsNearbyDuplicate(n, m))

        # def test6(self):
        #     n = 8
        #     ans = 35
        #     self.assertEqual(ans, self.sol.containsNearbyDuplicate(n, m), ans)


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
