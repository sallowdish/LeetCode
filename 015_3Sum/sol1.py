class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        else:
            length = len(nums)
        reval = set()
        nums = sorted(nums)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        reval.add((nums[i],nums[j],nums[k]))
        reval = sorted(sorted(sorted(reval,key = lambda x:x[2]), key = lambda x:x[1]), key = lambda x:x[0])
        return [list(x) for x in reval]
