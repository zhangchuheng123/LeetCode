# DP
# f[i][j]: whether s[:i] matches p[:j]

class Solution:
    def match(self, s, p):
        return (s == p) or (p == '.')

    def isMatch(self, s, p):

        lens, lenp = len(s), len(p)

        f = [[False for _ in range(lenp+1)] for _ in range(lens+1)]
        f[0][0] = True

        for j in range(lenp):
            # 'x* to match empty string
            f[0][j+1] = f[0][j-1] and p[j] == '*'
            for i in range(lens):
                if p[j] == '*':
                    # match for the first time or multiple times
                    f[i+1][j+1] = (self.match(s[i], p[j-1]) and (f[i][j-1] or f[i][j+1]))
                    # match for zero time
                    f[i+1][j+1] = f[i+1][j+1] or f[i+1][j-1]
                    # Pay attention to the the boundary condition here 
                else:
                    f[i+1][j+1] = self.match(s[i], p[j]) and f[i][j]
        
        return f[lens][lenp]