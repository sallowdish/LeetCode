class Solution(object):
    def getPermutation(self, n, k):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = list(range(1, n + 1))
        P = [""]
        for n in nums:
            P_bar = []
            for p in P:
                for i in range(len(p) + 1):
                    P_bar.append(p[:i] + str(n) + p[i:])
            P = P_bar
        return sorted(P)[k - 1]
