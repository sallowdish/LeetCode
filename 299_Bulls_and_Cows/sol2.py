class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s = list(secret)
        g = list(guess)
        ds = {}
        dg = {}
        bull = cow = 0
        # find bull
        i = 0
        while i < len(s):
            if s[i] == g[i]:
                bull += 1
                del s[i]
                del g[i]
            else:
                if s[i] in ds:
                    ds[s[i]] += 1
                else:
                    ds[s[i]] = 1
                if g[i] in dg:
                    dg[g[i]] += 1
                else:
                    dg[g[i]] = 1
                i += 1
        for k in dg.keys():
            if k in ds:
                cow += min(ds[k], dg[k])
        return "%dA%dB" % (bull, cow)
