class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 0:
            raise ValueError('n has to be non-negative')
        if n == 0:
            return []
        target = 2 ** n
        is_0_to_1 = True
        is_from_right = False
        ret = ["0" * n]
        while len(ret) < target:
            last = ret[-1]
            next = Solution.find_next(last, is_0_to_1, is_from_right)
            if next is None or next in ret:
                is_0_to_1 = not is_0_to_1
            else:
                ret.append(next)
                is_from_right = not is_from_right

        print(ret)
        return [int(x, 2) for x in ret]

    @staticmethod
    def find_next(prev, is_0_to_1, is_from_right):
        ret = None
        if is_from_right:
            prev = prev[::-1]
        for i in range(len(prev)):
            val = prev[i]
            if (is_0_to_1 and val == "0") or (not is_0_to_1 and val == '1'):
                ret = prev[:i] + str(1 - int(val)) + prev[i + 1:]
        if ret is None:
            return None
        if is_from_right:
            return ret[::-1]
        else:
            return ret
