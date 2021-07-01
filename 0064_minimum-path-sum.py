# 给定一个包含非负整数的 mxn 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

# 示例 1：
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。

# 示例 2：
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12

# 提示：

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100

MAXN = 200 * 200 * 100 + 1

class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        minlen = [0] * n 
        minlen[0] = grid[0][0]
        for j in range(1, n):
            minlen[j] = minlen[j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(n):
                minlen[j] = min(minlen[j-1] if j > 0 else MAXN, minlen[j]) + grid[i][j]
                
        return minlen[n-1]

if __name__ == '__main__':
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(Solution().minPathSum([[1,2,3],[4,5,6]]))