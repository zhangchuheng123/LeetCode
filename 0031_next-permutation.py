# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须 原地 修改，只允许使用额外常数空间。

# 示例 1：

# 输入：nums = [1,2,3]
# 输出：[1,3,2]
# 示例 2：

# 输入：nums = [3,2,1]
# 输出：[1,2,3]
# 示例 3：

# 输入：nums = [1,1,5]
# 输出：[1,5,1]
# 示例 4：

# 输入：nums = [1]
# 输出：[1]

# Solution:
#   Step 1: find non-increasing from last, nums[i]
#   Step 2: find the minimum element among the elements till i that are larger than nums[i], nums[j]
#   Step 3: swap i and j
#   Step 4: turn decreasing seq into increasing seq

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        # Step 1
        last = None
        i = n - 1
        while i >= 0:
            if last is None:
                last = nums[i]
            elif nums[i] < last:
                break
            else:
                last = nums[i]
            i -= 1

        # Step 2
        minval = 101
        minind = None
        if i > -1:
            for j in reversed(range(i + 1, n)):
                if nums[j] > nums[i] and nums[j] < minval:
                    minval = nums[j]
                    minind = j  
        j = minind


        # Step 3
        if j is not None:
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4
        p, q = i+1, n-1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1

if __name__ == '__main__':

    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    print(nums)

    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    print(nums)

    nums = [1, 1, 5]
    Solution().nextPermutation(nums)
    print(nums)

    nums = [1]
    Solution().nextPermutation(nums)
    print(nums)

    nums = [1, 1]
    Solution().nextPermutation(nums)
    print(nums)


