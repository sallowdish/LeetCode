class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        next_step = set()
        next_step.add(len(nums) - 1)
        while next_step:
            step = next_step.pop()
            count = 1
            for i in range(step - 1, -1, -1):
                if nums[i] >= count:
                    if i == 0:
                        return True
                    next_step.add(i)
                count += 1
        return False
