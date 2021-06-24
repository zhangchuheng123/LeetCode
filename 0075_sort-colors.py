# O(n) algorithm to sort 3 numbers

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        j = length - 1
        while i < j:
            if nums[i] == 2 and nums[j] != 2:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] != 2:
                i += 1
            if nums[j] == 2:
                j -= 1
        
        i = 0
        while i < j:
            if nums[i] != 0 and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[j] != 0:
                j -= 1
            if nums[i] == 0:
                i += 1 
            