# Solution: Dynamic programming
# Key: use a '#' to simplify boundary conditions

MAXN = 1001

class Solution:
    def minDistance(self, word1, word2):
        word1 = '#' + word1
        word2 = '#' + word2
        len1 = len(word1)
        len2 = len(word2)

        f = [[max(i, j) for i in range(len2)] for j in range(len1)]

        for i in range(1, len1):
            for j in range(1, len2):
                c1 = f[i-1][j] + 1
                c2 = f[i][j-1] + 1
                c3 = f[i-1][j-1] if word1[i] == word2[j] else f[i-1][j-1] + 1
                f[i][j] = min(c1, c2, c3)
                
        return f[len1-1][len2-1]