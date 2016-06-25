class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                if counter == 0:
                    counter += 1
                else:
                    del nums[index]
                    continue
            else:
                counter = 0
            index += 1
        return len(nums)
