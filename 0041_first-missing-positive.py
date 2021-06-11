class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        n1 = n + 1

        for i in range(n):
            if nums[i] > n or nums[i] <= 0:
                nums[i] = n1

        for i in range(n):
            number = abs(nums[i])
            if number != n1:
                nums[number - 1] = - abs(nums[number - 1]) 
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
