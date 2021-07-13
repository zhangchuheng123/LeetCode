# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

# 请你找出符合题意的 最短 子数组，并输出它的长度。

# 示例 1：
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

# 示例 2：
# 输入：nums = [1,2,3,4]
# 输出：0

# 示例 3：
# 输入：nums = [1]
# 输出：0

# 提示：

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = [(0, nums[0])]
        i = 1
        while i < len(nums) and nums[i] >= stack[-1][1]:
            stack.append((i, nums[i]))
            i += 1
        while i < len(nums):
            while len(stack) > 0 and nums[i] < stack[-1][1]:
                stack.pop()
            i += 1

        i = len(stack)
        if i == len(nums):
            return 0

        stack = [(len(nums) - 1, nums[len(nums) - 1])]
        j = len(nums) - 2
        while j >= 0 and nums[j] <= stack[-1][1]:
            stack.append((j, nums[j]))
            j -= 1
        while j >= 0:
            while len(stack) > 0 and nums[j] > stack[-1][1]:
                stack.pop()
            j -= 1
        j = len(stack)
        return len(nums) - i - j

