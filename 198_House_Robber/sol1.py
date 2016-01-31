class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(nums[0]+self.rob(nums[2:]), nums[1]+self.rob(nums[3:]))