# 给定一个不含重复数字的数组 nums ，返回其所有可能的全排列。你可以按任意顺序返回答案。

# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# 示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]

# 示例 3：
# 输入：nums = [1]
# 输出：[[1]]

# 提示：

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数互不相同

class Solution:
    def permute(self, nums):
        ans = []
        self.search(ans, nums, 0)
        return ans

    def search(self, ans, nums, depth):
        if depth == len(nums) - 1:
            ans.append(nums.copy())
        else:
            for i in range(depth, len(nums)):
                nums[depth], nums[i] = nums[i], nums[depth]
                self.search(ans, nums, depth+1)
                nums[depth], nums[i] = nums[i], nums[depth]

if __name__ == '__main__':
    print(Solution().permute([1, 2, 3, 4]))
    print(Solution().permute([1, 0]))
    print(Solution().permute([1]))