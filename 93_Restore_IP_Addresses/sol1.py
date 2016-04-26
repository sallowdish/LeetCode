import re


class Solution(object):
    def __init__(self):
        self.ret = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        init_position = Solution.determine_initial_postion(s)
        self.rec_construct_possible_ip(s, init_position)
        return self.ret

    def rec_construct_possible_ip(self, s, dot_positions):
        ip_candidate = ".".join(Solution.parse_ip_address(s, dot_positions))
        if Solution.is_valid_ip(ip_candidate) and ip_candidate not in self.ret:
            self.ret.append(ip_candidate)
        next_positions = Solution.find_next_possible_dot_position(len(s), dot_positions)
        for next_position in next_positions:
            self.rec_construct_possible_ip(s, next_position)

    @staticmethod
    def parse_ip_address(s, dot_positions):
        return (s[:dot_positions[0]], s[dot_positions[0]:dot_positions[1]], s[dot_positions[1]:dot_positions[2]],
                s[dot_positions[2]:])

    @staticmethod
    def find_next_possible_dot_position(length, dot_position):
        ret = []
        if dot_position[2] < length - 1 and dot_position[2] - dot_position[1] < 3:
            ret.append((dot_position[0], dot_position[1], dot_position[2] + 1))
        if dot_position[1] < dot_position[2] - 1 and dot_position[1] - dot_position[0] < 3:
            ret.append((dot_position[0], dot_position[1] + 1, dot_position[2]))
        if dot_position[0] < dot_position[1] - 1 and dot_position[0] < 3:
            ret.append((dot_position[0] + 1, dot_position[1], dot_position[2]))
        return tuple(ret)

    @staticmethod
    def is_valid_ip(s):
        re_exp = "^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]?)$"
        return bool(re.match(re_exp, s))

    @staticmethod
    def determine_initial_postion(s):
        if len(s) < 7:
            return (1, 2, 3)
        d = {7: (1, 2, 4), 8: (1, 2, 5), 9: (1, 3, 6), 10: (1, 4, 7), 11: (2, 5, 8), 12: (3, 6, 9)}
        return d[len(s)]
