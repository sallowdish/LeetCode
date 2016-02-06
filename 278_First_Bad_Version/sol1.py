# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 5


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        elif n == 1:
            return n if isBadVersion(n) else None
        else:
            if isBadVersion(1):
                return 1
            elif not isBadVersion(n):
                return None
            else:
                return self.rec_first_bad_version(1, n)

    def rec_first_bad_version(self, start, end):
        if end == start + 1:
            return end
        else:
            half = int((start + end) / 2)
            if isBadVersion(half):
                return self.rec_first_bad_version(start, half)
            else:
                return self.rec_first_bad_version(half, end)
