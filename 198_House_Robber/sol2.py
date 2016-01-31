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
        max_money = [0, nums[0]]
        for i in range(1, len(nums)):
            max_money.append(max(max_money[i - 1] + nums[i], max_money[i]))
        return max_money[-1]
