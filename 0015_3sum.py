class Solution:
    def threeSum(self, nums):

        nums = sorted(nums)
        n = len(nums)
        ans = []

        for i, a1 in enumerate(nums):
            if i == 0 or a1 != nums[i-1]:
                p = n - 1
                for j in range(i+1, n):
                    a2 = nums[j]
                    if j == i+1 or a2 != nums[j-1]:
                        while a1 + a2 + nums[p] > 0 and p - 1 > j:
                            p -= 1
                        if p <= j:
                            break
                        if a1 + a2 + nums[p] == 0:
                            ans.append([a1, a2, nums[p]])

        return ans