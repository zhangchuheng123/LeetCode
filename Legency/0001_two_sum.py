class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(0, l):
            j0 = min(i + 1, l)
            for j in range(j0, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return 0
