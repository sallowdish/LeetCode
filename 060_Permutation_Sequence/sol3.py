class Solution(object):
    def getPermutation(self, n, k):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if n == 1 and k == 1:
            return "1"
        permutation_count = [1]
        for i in range(2, n):
            permutation_count.append(permutation_count[-1] * i)
        candidates = [i for i in range(1, n + 1)]
        ret = ""
        for threshold in permutation_count[::-1]:
            q = k // threshold
            r = k % threshold
            index = q if r > 0 else q - 1
            ret += str(candidates[index])
            del candidates[index]
            k = r
        return ret + str(candidates[0])
