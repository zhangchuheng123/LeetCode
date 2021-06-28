class Solution:
    def maxProduct(self, nums):
        length = len(nums)
        fmax = [nums[0]]
        fmin = [nums[0]]
        ans = nums[0]
        for i in range(1, length):
            fmax.append(max(nums[i], fmax[i-1] * nums[i], fmin[i-1] * nums[i]))
            fmin.append(min(nums[i], fmax[i-1] * nums[i], fmin[i-1] * nums[i]))
            if fmax[-1] > ans:
                ans = fmax[-1]
        return ans

if __name__ == '__main__':
    print(Solution().maxProduct([-4,-3,-2]))