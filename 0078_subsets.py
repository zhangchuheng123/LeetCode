class Solution:

    def subsets(self, nums):
        l = len(nums)
        ans = []
        for binary in range(1 << l):
            ans.append([nums[i] for i in range(l) if (1 << i) & binary])
        return ans