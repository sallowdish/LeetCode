class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base26 = list(baseN(n, 26))
        base26Val = [self.digitToValue(x) for x in base26]
        base26Val = self.merge(base26Val)
        while not base26Val[0]:
            del base26Val[0]
        return "".join([chr(x + 64) for x in base26Val])

    def digitToValue(self, c):
        numerals="0123456789abcdefghijklmnopqrstuvwxyz"
        return numerals.index(c)

    def merge(self, l):
        for i in range(1, len(l)):
            if l[-i] == 0:
                # borrow
                isFound =False
                j = i + 1
                while 1:
                    if j > len(l):
                        break
                    if l[-j] != 0:
                        isFound = True
                        break
                    j += 1
                if isFound:
                    l[-j] -= 1
                    j -= 1
                    while j >= i:
                        l[-j] = 26
                        j -= 1
                else:
                    break
        return l


def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])