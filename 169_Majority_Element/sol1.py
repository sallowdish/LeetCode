class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        threshold = int(len(nums) / 2)
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            if dic[i] >  threshold:
                    return i