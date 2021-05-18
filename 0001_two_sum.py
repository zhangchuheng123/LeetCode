class Solution:
    def twoSum(self, nums, target):
        hashmap = {num:ind for ind,num in enumerate(nums)}
        for i, num1 in enumerate(nums):
            j = hashmap.get(target - num1)
            if j is not None and i != j:
                return [i, j]