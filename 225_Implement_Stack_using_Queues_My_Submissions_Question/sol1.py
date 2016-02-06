class Stack(object):
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
        if not self.empty():
            del self.data[-1]

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.data[-1]
        else:
            return None

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.data) == 0
