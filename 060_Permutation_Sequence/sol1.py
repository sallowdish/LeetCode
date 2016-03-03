class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n + 1))
        return "".join(self.rec_permute("", nums)[k - 1])

    def rec_permute(self, root, candidates):
        if not candidates:
            return [root]
        P = []
        for i in candidates:
            P += self.rec_permute(root + str(i), [x for x in candidates if i !=
                                                  x])
        return P
