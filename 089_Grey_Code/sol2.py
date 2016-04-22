class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return []
        ret = ['0', '1']
        c = 1
        while c < n:
            is_0_first = True
            next_row = []
            for raw in ret:
                next_row += [raw + "0", raw + "1"] if is_0_first else [raw + '1', raw + '0']
                is_0_first = not is_0_first
            ret = next_row
            c += 1
        return [int(x, 2) for x in ret]
