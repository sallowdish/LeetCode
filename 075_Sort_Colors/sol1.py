class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        colors = enumerate(['red', 'white', 'blue'])
        red = white = blue = 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
            else:
                blue += 1
        sorted_nums = [0] * red + [1] * white + [2] * blue
        # for i in len(nums):
        #     nums[i] = sorted_nums[i]
        return sorted_nums
