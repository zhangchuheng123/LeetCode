import time


class Solution(object):
    __TYPE_NULL = 0
    __TYPE_SINGLE_CH = 1
    __TYPE_MULTIPLE_CH = 2
    __TYPE_MULTIPLE_ANY = 3

    def isMatch(self, s, p):
        p = self.prune(p)
        return self.is_match(s, p)

    def is_match(self, s, p):
        """
        :type s: str
        :type p: pattern str
        :rtype: bool
        """
        type1, ch1 = self.get_first(s)
        type2, ch2 = self.get_first(p)

        if type1 == self.__TYPE_NULL:
            if type2 == self.__TYPE_NULL:
                return True
            elif type2 == self.__TYPE_SINGLE_CH:
                return False
            else:
                return self.is_match(s, p[2:])
        else:
            if type2 == self.__TYPE_NULL:
                return False
            elif type2 == self.__TYPE_SINGLE_CH:
                if (ch1 == ch2) or (ch2 == '.'):
                    return self.is_match(s[1:], p[1:])
                else:
                    return False
            elif type2 == self.__TYPE_MULTIPLE_CH:
                if ch1 == ch2[0]:
                    return self.is_match(s[1:], p[2:]) or self.is_match(s, p[2:]) or self.is_match(s[1:], p)
                else:
                    return self.is_match(s, p[2:])
            else:
                return self.is_match(s[1:], p[2:]) or self.is_match(s, p[2:]) or self.is_match(s[1:], p)

    def get_first(self, s):
        if len(s) == 0:
            return self.__TYPE_NULL, ''
        if (len(s) >= 2) and (s[1] == '*'):
            if s[0] == '.':
                return self.__TYPE_MULTIPLE_ANY, s[0:2]
            else:
                return self.__TYPE_MULTIPLE_CH, s[0:2]
        else:
            return self.__TYPE_SINGLE_CH, s[0]

    @staticmethod
    def prune(p):
        pos = 0
        while pos <= len(p):
            if len(p)-pos < 4:
                return p
            if p[pos+1] == p[pos+3] == '*':
                if p[pos] == '.':
                    p = p[:pos+2] + p[pos+4:]
                elif p[pos+2] == '.':
                    p = p[:pos] + p[pos+2:]
                elif p[pos] == p[pos+2]:
                    p = p[:pos] + p[pos + 2:]
                else:
                    pos += 2
            else:
                pos += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch("a", ""))  # True
    start = time.clock()
    print(solution.isMatch("aaaaaaaaaaaaa", "a*a*a*a*a*a*a*a*a*a*c"))
    end = time.clock()
    print(end-start)
    print(solution.isMatch("a", "a*a"))             # True
    print(solution.isMatch("aa", "a*"))             # True
    print(solution.isMatch("a", "aa"))              # False
    print(solution.isMatch("aa", "aa"))             # True
    print(solution.isMatch("aaa", "aa"))            # False
    print(solution.isMatch("aa", "a*"))             # True
    print(solution.isMatch("aab", "c*a*b"))         # True
    print(solution.isMatch("aaa", "a.a"))           # True
    print(solution.isMatch("aca", "a.a"))           # True
    print(solution.isMatch("aac", "a.a"))           # False
    print(solution.isMatch("aac", "a..*.*.*c"))     # True
    print(solution.isMatch("a", "ab*"))             # True
    print(solution.isMatch("aa", ".*"))             # True
    print(solution.isMatch("a", ""))                # True
