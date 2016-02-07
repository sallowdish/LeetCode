class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            raise ValueError("Invalid input value")
        elif n < 4:
            return True
        elif n < 5:
            return False
        else:
            winRecord = [None, True, True, True, False]
            index = 5
            while index <= n:
                isCanWInNim = not (winRecord[index - 1] and winRecord[index - 2] and winRecord[index - 3])
                winRecord.append(isCanWInNim)
                index += 1
            return winRecord[-1]
