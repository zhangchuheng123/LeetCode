# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。
# 如果 i - 1 或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
# 求所能获得硬币的最大数量。

# 示例 1：
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# 示例 2：
# 输入：nums = [1,5]
# 输出：10

# 提示：

# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100

# n = 6
# [0 1 2 3 4 5]
# [1 3 1 5 8 1]

class Solution:
    def maxCoins(self, nums):
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        for width in range(3, n + 1):                        
            for i in range(n - width + 1):              
                j = i + width - 1                       
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], nums[i] * nums[k] * nums[j] + f[i][k] + f[k][j])
        return f[0][n-1]