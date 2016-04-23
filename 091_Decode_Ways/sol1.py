class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        ret = [1]
        s = "0" + s
        for i in range(1, len(s)):
            if i == 1:
                ret.append(1)
            else:
                if s[i] != "0":
                    val = int(s[i - 1:i + 1], 10)
                    if val > 10 and val < 27:
                        ret.append(ret[-1] + ret[-2])
                    else:
                        ret.append(ret[-1])
                else:
                    if s[i - 1] == "0" or int(s[i - 1]) > 2:
                        # invalid sequence
                        return 0
                    else:
                        val = int(s[i - 2:i], 10)
                        if val > 10 and val < 27:
                            ret.append(ret[-2])
                        else:
                            ret.append(ret[-1])
        return ret[-1]
