class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numCount = {}
        for n in nums:
            if n in numCount:
                numCount[n] += 1
            else:
                numCount[n] = 1
        for n in nums:
            numCount[n] -= 1
            diff = target - n
            if diff in numCount and numCount[diff] > 0:
                i = nums.index(n)
                if n == diff:
                    j = len(nums) - 1 - nums[::-1].index(diff)
                else:
                    j = nums.index(diff)
                return (i, j)