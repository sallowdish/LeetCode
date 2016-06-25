class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            raise ValueError("k cannot be larger than n.")
        if k == n:
            return [list(range(1, n + 1)), ]
        candidates = list(range(1, n + 1))
        chip = candidates[:k]
        index = k - 1
        ret = [chip[:]]
        while (1):
            chip = self.next_combination(chip, n)
            if chip:
                ret.append(chip[:])
            else:
                break
        return ret

    def next_combination(self, current_chip, n):
        if current_chip[-1] < n:
            current_chip[-1] += 1
            return current_chip
        k = len(current_chip)
        index = (k - 1)
        while index - 1 >= 0:
            index -= 1
            if current_chip[index] < n - ((k - 1) - index):
                current_chip[index] += 1
                for i in range(index + 1, k):
                    current_chip[i] = current_chip[i - 1] + 1
                return current_chip
            else:
                continue
        return None
