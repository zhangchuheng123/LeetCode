# 整数数组 nums 按升序排列，数组中的值互不相同 。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

# 给你旋转后的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1。

# 示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4

# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1

# 示例 3：
# 输入：nums = [1], target = 0
# 输出：-1

class Solution:
    def search(self, nums, target):

        n = len(nums)
        l, r = 0, n - 1

        # 要注意二分查找的基本框架，就是要迭代每次把潜在的区域缩小一半
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[l]:
                # the right part is ordered
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # the left part is ordered
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

if __name__ == '__main__':
    print(Solution().search([4,5,6,7,0,1,2], 0), end=' = ')
    print(4)

    print(Solution().search([4,5,6,7,0,1,2], 3), end=' = ')
    print(-1)

    print(Solution().search([1], 1), end=' = ')
    print(0)
    
    print(Solution().search([2], 3), end=' = ')
    print(-1)
