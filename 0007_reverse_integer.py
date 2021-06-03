class Solution:
    def reverse(self, x):
        maxn = '2147483648'
        len_maxn = 10
        strx = str(x)
        if strx[0] == '-':
            num = strx[:0:-1]
            if len(num) < len_maxn or num <= maxn:
                stry = '-' + num
            else:
                return 0
        else:
            num = strx[::-1]
            if len(num) < len_maxn or num < maxn:
                stry = num
            else:
                return 0
        return int(stry)