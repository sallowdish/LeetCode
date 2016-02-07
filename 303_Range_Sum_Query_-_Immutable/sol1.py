class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.range_sums = {}
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    self.range_sums[(i, j)] = nums[i]
                else:
                    self.range_sums[(i, j)] = self.range_sums[(i, j - 1)] + nums[j]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.range_sums[(i, j)]



        # Your NumArray object will be instantiated and called as such:
        # numArray = NumArray(nums)
        # numArray.sumRange(0, 1)
        # numArray.sumRange(1, 2)
