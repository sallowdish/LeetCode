#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import *


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    # whole test
    def test0_0(self):
        ip = "11.1.1.11"
        ans = True
        self.run_test_is_valid_ip(ip, ans)

    def test0_1(self):
        ip = "111.111.245.11"
        ans = True
        self.run_test_is_valid_ip(ip, ans)

    def test0_2(self):
        ip = "255.255.255.256"
        ans = False
        self.run_test_is_valid_ip(ip, ans)

    def test1_0(self):
        length = 4
        dot_position = (1, 2, 3)
        ans = ()
        self.run_test_find_next_possible_dot_position(length, dot_position, ans)

    def test1_1(self):
        length = 5
        dot_position = (1, 2, 3)
        ans = ((1, 2, 4),)
        self.run_test_find_next_possible_dot_position(length, dot_position, ans)

    def test1_2(self):
        length = 6
        dot_position = (1, 3, 5)
        ans = ((1, 4, 5), (2, 3, 5))
        self.run_test_find_next_possible_dot_position(length, dot_position, ans)

    # whole test
    def test2_0(self):
        s = "1111"
        ans = ["1.1.1.1", ]
        self.run_test(s, ans)

    def test2_1(self):
        s = "11111"
        ans = ["1.1.1.11", "1.1.11.1", "1.11.1.1", "11.1.1.1"]
        self.run_test(s, ans)

    def test2_2(self):
        s = "111611"
        ans = ["1.1.16.11", "1.1.161.1", "1.11.6.11", "1.11.61.1", "1.116.1.1", "11.1.6.11", "11.1.61.1", "11.16.1.1",
               "111.6.1.1"]
        self.run_test(s, ans)

    def test2_3(self):
        s = "122111"
        ans = ["1.2.2.111", "1.2.21.11", "1.2.211.1", "1.22.1.11", "1.22.11.1", "1.221.1.1", "12.2.1.11", "12.2.11.1",
               "12.21.1.1", "122.1.1.1"]
        self.run_test(s, ans)

    def test3_0(self):
        s = "25525511135"
        ans = ['255.255.11.135', '255.255.111.35']
        self.run_test(s, ans)

    def test3_1(self):
        s = "010010"
        ans = ["0.10.0.10", "0.100.1.0"]
        self.run_test(s, ans)

    def run_test(self, s, ans):
        ret = self.sol.restoreIpAddresses(s)
        self.assertEqual(sorted(ans), sorted(ret))

    def run_test_is_valid_ip(self, ip, ans):
        self.assertEqual(ans, self.sol.is_valid_ip(ip))

    def run_test_find_next_possible_dot_position(self, length, dot_position, ans):
        self.assertEqual(ans, self.sol.find_next_possible_dot_position(length, dot_position))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
