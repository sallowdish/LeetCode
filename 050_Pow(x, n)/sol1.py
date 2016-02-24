class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        const_max_int = 2147483647

        if x == 1 or n == 0:
            return 1
        is_positive = n > 0
        n = abs(n)
        if n % 2 == 0:
            power = self.myPow(x*x, n/2)
        else:
            power = x * self.myPow(x*x, (n-1)/2)

        power = const_max_int if power > const_max_int else power
        power = -const_max_int - 1 if power < -const_max_int - 1 else power
        return power if is_positive else 1/power
