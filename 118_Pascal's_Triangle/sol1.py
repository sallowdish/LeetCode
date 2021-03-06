class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        ret = [[1]]
        for i in range(2, numRows + 1):
            prev_line = ret[i - 1 - 1]
            new_line = []
            for j in range(i):
                if j == 0 or j == i -1:
                    new_line.append(1)
                elif j > int(i/2):
                    new_line.append(new_line[i - j - 1])
                else:
                    new_line.append(prev_line[j - 1] + prev_line[j])
            ret.append(new_line)
        return ret
