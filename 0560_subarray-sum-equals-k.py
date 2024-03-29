# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

# 示例 1 :
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

# 说明 :
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = {0: 1}
        curr_sum = 0
        ans = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in presum:
                ans += presum[curr_sum - k]
            if curr_sum in presum:
                presum[curr_sum] += 1
            else:
                presum[curr_sum] = 1
        return ans