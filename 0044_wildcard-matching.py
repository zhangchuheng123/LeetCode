class Solution:
    def isMatch(self, s, p):
        s = '#' + s
        p = '#' + p
        length_s = len(s)
        length_p = len(p)

        f = [True] + [False for _ in range(1, length_s)]
        g = [False for _ in range(length_s)]
        # f[i][j] whether match till p[i] and s[j]

        for i in range(1, length_p):

            if p[i] == '*':
                g[0] = f[0]
            else:
                g[0] = False

            for j in range(1, length_s):
                if p[i] == '?' or p[i] == s[j]:
                    g[j] = f[j-1]
                elif p[i] == '*':
                    g[j] = g[j-1] | f[j-1] | f[j]
            f = g
            g = [False for _ in range(length_s)]

        return f[-1]

if __name__ == '__main__':
    print(Solution().isMatch('aa', 'a'))
    print(Solution().isMatch('aa', '*'))
    print(Solution().isMatch('cb', '?a'))
    print(Solution().isMatch('adceb', '*a*b'))
    print(Solution().isMatch('acdcb', 'a*c?b'))