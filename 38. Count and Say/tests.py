#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution

class Test(TestCase):
    sol = None
    ans = ["1", "11", "21", "1211", "111221"]

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        n = 1
        self.assertEqual(self.sol.countAndSay(n) ,self.ans[n - 1])

    def test1(self):
        n = 2
        self.assertEqual(self.sol.countAndSay(n) ,self.ans[n - 1])

    def test2(self):
        n = 3
        self.assertEqual(self.sol.countAndSay(n) ,self.ans[n - 1])

    def test3(self):
        n = 4
        self.assertEqual(self.sol.countAndSay(n) ,self.ans[n - 1])

    def test4(self):
        n = 5
        self.assertEqual(self.sol.countAndSay(n) ,self.ans[n - 1])




if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
