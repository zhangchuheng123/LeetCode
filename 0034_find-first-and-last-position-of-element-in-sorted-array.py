# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 进阶：

# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]

# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]

# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]

class Solution:
    def searchRange(self, nums, target):
        left_ind = self.binary_search_left(nums, target)
        if left_ind == -1:
            return [-1, -1]
        else:
            right_ind = self.binary_search_right(nums, target)
            return [left_ind, right_ind]

    def binary_search_left(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, mid, r, nums[mid])

            if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                return mid

            if target <= nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
        return -1

    def binary_search_right(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target and (mid == n - 1 or nums[mid+1] > target):
                return mid

            if target < nums[mid]:
                r = mid - 1
            elif target >= nums[mid]:
                l = mid + 1
        return -1

if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10], 8), end=' = ')
    print('[3, 4]')

    print(Solution().searchRange([5,7,7,8,8,10], 6), end=' = ')
    print('[-1, -1]')

    print(Solution().searchRange([], 0), end=' = ')
    print('[-1, -1]')
