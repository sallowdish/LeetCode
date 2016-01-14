class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        count = 0
        totalLength = float(len(nums1) + len(nums2))
        while count < totalLength / 2 - 1:
            self.merge(nums1,nums2)
            count += 1
        if (totalLength) %2 != 0:
            return self.merge(nums1,nums2, 1)
        else:
            op1 = self.merge(nums1, nums2, 1)
            op2 = self.merge(nums1, nums2, 1)
            return (float(op1) + op2) / 2

    def merge(self, nums1, nums2, flag = False):
        if flag:
            if len(nums1) == 0:
                return nums2.pop(0)
            elif len(nums2) == 0:
                return nums1.pop(0)
            return nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0)
        else:
            if len(nums1) == 0:
                del nums2[0]
            elif len(nums2) == 0:
                del nums1[0]
            else:
                if nums1[0] < nums2[0]:
                    del nums1[0]
                else:
                    del nums2[0]