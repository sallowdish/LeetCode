class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s = list(secret)
        g = list(guess)
        toDel = []
        bull = cow = 0
        # find bull
        for i in range(len(guess)):
            if s[i] == g[i]:
                bull += 1
                toDel.append(i)
        s = [s[i] for i in range(len(s)) if i not in toDel]
        g = [g[i] for i in range(len(g)) if i not in toDel]
        for i in g:
            if i in s:
                cow += 1
                s.remove(i)
        return "%dA%dB" % (bull, cow)
