class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if not self.isOverLap(((A, B), (C, D)), ((E, F), (G, H))):
            return 0
        return 1

    def isOverLap(self, rec_1, rec_2):
        full_rec_1 = (rec_1_point_A, rec_1_point_B, rec_1_point_C, rec_1_point_D) = (
        rec_1[0], (rec_1[1][0], rec_1[0][1]), rec_1[1], (rec_1[0][0], rec_1[1][1]))
        overlap_status_1 = list(map(lambda x: self.is_point_in_rec(x, rec_2), full_rec_1))
        if True in overlap_status_1:
            return ([full_rec_1[i] for i in range(4) if overlap_status_1[i] == True], rec_2)
        full_rec_2 = (rec_2_point_A, rec_2_point_B, rec_2_point_C, rec_2_point_D) = (
        rec_2[0], (rec_2[1][0], rec_2[0][1]), rec_2[1], (rec_2[0][0], rec_2[1][1]))
        overlap_status_2 = list(map(lambda x: self.is_point_in_rec(x, rec_1), full_rec_2))
        if True in overlap_status_2:
            return ([full_rec_2[i] for i in range(4) if overlap_status_2[i] == True], rec_1)
        return False

    def is_point_in_rec(self, point, rec):
        bottom_left_point = rec[0]
        top_right_point = rec[1]
        return bottom_left_point[0] < point[0] < top_right_point[0] and bottom_left_point[1] < point[1] < \
                                                                        top_right_point[1]
