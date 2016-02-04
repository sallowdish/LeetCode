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
        recA = ((A, B), (C, D))
        recB = ((E, F), (G, H))
        recC = ((max(A, E), max(B, F)), (min(C, G), min(D, H)))

        if recC[0][0] < recC[1][0] and recC[0][1] < recC[1][1]:
            return self.rec_area(recA[0],recA[1]) + self.rec_area(recB[0], recB[1])-self.rec_area(recC[0], recC[1])
        return self.rec_area(recA[0],recA[1]) + self.rec_area(recB[0], recB[1])

    def rec_area(self, point_a, point_b):
        width = abs(point_a[0] - point_b[0])
        height = abs(point_a[1] - point_b[1])
        return width * height