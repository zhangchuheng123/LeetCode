class Solution:
    def myPow(self, x, n):

        if n < 0:
            n = -n
            is_negative = True
        else:
            is_negative = False

        ans = 1
        tmp = x
        while n > 0:
            if n & 0b1:
                ans *= tmp
            tmp = tmp * tmp
            n = n >> 1
        if is_negative:
            ans = 1 / ans
        return ans