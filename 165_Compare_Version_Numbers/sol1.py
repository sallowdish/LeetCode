class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        flag = 0
        while len(v1) > 0 and len(v2) > 0:
            if v1[0] > v2[0]:
                return 1
            if v1[0] < v2[0]:
                return -1
            del v1[0]
            del v2[0]
        if len(v1) > 0:
            v1 = [x for x in v1 if x]
            return 1 if len(v1) else 0
        elif len(v2) > 0:
            v2 = [x for x in v2 if x]
            return -1 if len(v2) else 0
        else:
            return 0