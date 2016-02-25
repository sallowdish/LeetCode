class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target_index = len(nums) - 1
        if target_index == 0:
            return True
        while target_index > 0:
            is_proceed = False
            # xrange for py2
            for i in range(1, target_index + 1):
                if nums[target_index - i] >= i:
                    target_index = target_index - i
                    is_proceed = True
                    break
            if target_index == 0:
                return True
            if not is_proceed:
                return False
        return False
