class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.range_sums = []
        for i in range(len(nums)):
            if i == 0:
                self.range_sums.append(nums[0])
            else:
                self.range_sums.append(nums[i] + self.range_sums[-1])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.range_sums[j]
        return self.range_sums[j] - self.range_sums[i] + self.nums[i]



        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.sumRange(1, 2)
