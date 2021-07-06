# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 你可以认为每种硬币的数量是无限的。

# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1

# 示例 2：
# 输入：coins = [2], amount = 3
# 输出：-1

# 示例 3：
# 输入：coins = [1], amount = 0
# 输出：0

# 示例 4：
# 输入：coins = [1], amount = 1
# 输出：1

# 示例 5：
# 输入：coins = [1], amount = 2
# 输出：2

# 提示：

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

INF = 10001

class Solution:

    # BFS: Timeout
    # def coinChange(self, coins, amount):
    #     if amount == 0:
    #         return 0
    #     coins = sorted(coins, reverse=True)
    #     queue = [(0, amount)]
    #     while len(queue) > 0:
    #         num_coin_used, remaining_amount = queue.pop(0)
    #         for c in coins:
    #             if remaining_amount - c > 0:
    #                 queue.append((num_coin_used + 1, remaining_amount - c))
    #             elif remaining_amount == c:
    #                 return num_coin_used + 1
    #     return -1

    # DP
    def coinChange(self, coins, amount):
        f = [INF] * (amount + 1)
        f[0] = 0
        for curr_amount in range(1, amount + 1):
            for c in coins:
                if curr_amount - c >= 0:
                    f[curr_amount] = min(f[curr_amount], f[curr_amount - c] + 1)
        if f[amount] == INF:
            return -1
        else:
            return f[amount]