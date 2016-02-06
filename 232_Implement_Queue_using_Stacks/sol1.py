class Queue(object):
    data = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.play(1)

    def peek(self):
        """
        :rtype: int
        """
        return self.play(0)

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.data) == 0

    def play(self, is_remove):
        if len(self.data) == 0:
            return None
        elif len(self.data) == 1:
            if is_remove:
                ret = self.data[0]
                del self.data[0]
                return
            return self.data[0]
        else:
            tempList = []
            while len(self.data) > 1:
                tempList.append(self.data.pop())
            ret = self.data[0]
            if is_remove:
                del self.data[0]
            while len(tempList) > 0:
                self.data.append(tempList.pop())
            if is_remove:
                return
            return ret
