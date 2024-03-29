# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

# 示例:

# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：

# 所有输入均为小写字母。
# 不考虑答案输出的顺序。

class Solution:
    def groupAnagrams(self, strs):
        ans = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]
        output = []
        for key, val in ans.items():
            output.append(val)

        return output

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))