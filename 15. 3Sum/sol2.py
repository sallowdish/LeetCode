class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        nums = list(d.keys())
        length = len(nums)
        reval = set()
        for i in range(length):
            for j in range(i, length):
                    d[nums[i]] -= 1
                    d[nums[j]] -= 1
                    c= 0 - nums[i] -nums[j]
                    if d[nums[i]] >=0 and d[nums[j]] >=0 and c in d and d[c] > 0:
                        reval.add(tuple(sorted([nums[i],nums[j],c])))
                    d[nums[i]] += 1
                    d[nums[j]] += 1
        reval = sorted(sorted(sorted(reval,key = lambda x:x[2]), key = lambda x:x[1]), key = lambda x:x[0])
        return [list(x) for x in reval]
