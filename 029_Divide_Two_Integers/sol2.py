class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None
        if dividend == 0:
            return 0

        const_max_int = 2147483647

        is_positive = self.is_positive(dividend, divisor)
        bin_dividend = bin(abs(dividend))[2:]
        bin_divisor = bin(abs(divisor))[2:]

        if len(bin_dividend) < len(bin_divisor):
            return 0

        remainder = bin_dividend[:len(bin_divisor) - 1]
        ret = ""
        for i in range(len(bin_divisor) - 1, len(bin_dividend)):
            a = remainder + bin_dividend[i]
            if int(a, 2) >= int(bin_divisor, 2):
                ret += "1"
                remainder = bin(int(a, 2) - int(bin_divisor, 2))[2:]
            else:
                ret += "0"
                remainder = a
        ret_int = int(ret, 2)
        if not is_positive:
            ret_int = -ret_int
        if ret_int > const_max_int:
            return const_max_int
        elif ret_int < -const_max_int -1:
            return -const_max_int -1
        return ret_int

    def is_positive(self, a, b):
        flag = a > 0
        return flag if b > 0 else not flag
