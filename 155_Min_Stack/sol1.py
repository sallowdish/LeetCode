class MinStack(object):
    dataSet = None
    minIndex = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataSet = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.dataSet.append(x)
        if self.minIndex is None:
            self.minIndex = 0
        else:
            self.minIndex = len(self.dataSet) - 1 if x < self.dataSet[self.minIndex] else self.minIndex
        return self


    def pop(self):
        """
        :rtype: nothing
        """
        try:
            ret = self.dataSet.pop()
            if len(self.dataSet) == 0:
                self.minIndex = None
            elif self.minIndex == len(self.dataSet):
                self.minIndex = self.dataSet.index(min(self.dataSet))
            else:
                pass
            return ret

        except Exception:
            raise IndexError()

    def top(self):
        """
        :rtype: int
        """
        return self.dataSet[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.minIndex is None:
            return None
        return self.dataSet[self.minIndex]

