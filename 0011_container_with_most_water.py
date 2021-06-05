# Brute force: time O(n^2) space O(1)
# F[i][j] = min(a[i], a[j]) * abs(j - i)

# Double pointer: time O(n) space O(1)

class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxvol = 0
        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            if maxvol < vol:
                maxvol = vol
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxvol