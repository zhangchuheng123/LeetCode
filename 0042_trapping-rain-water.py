class Solution:
    def trap(self, height):
        n = len(height)
        if n <= 1:
            return 0
        l, lmaxind, lmax, lvol = 0, 0, height[0], 0
        r, rmaxind, rmax, rvol = n-1, n-1, height[n-1], 0

        total_vol = 0
        while l < r:
            if lmax <= rmax:
                l += 1
                if height[l] >= lmax:
                    total_vol += (l - lmaxind - 1) * lmax - lvol
                    lmaxind = l
                    lmax = height[l]
                    lvol = 0
                else:
                    lvol += height[l]
            else:
                r -= 1
                if height[r] >= rmax:
                    total_vol += (rmaxind - r - 1) * rmax - rvol
                    rmaxind = r
                    rmax = height[r]
                    rvol = 0
                else:
                    rvol += height[r]
                    
        return total_vol
