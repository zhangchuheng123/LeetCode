# 给你一个只包含 '('和 ')'的字符串，找出最长有效（格式正确且连续）括号子串的长度。

# 示例 1：
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"

# 示例 2：
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"

# 示例 3：
# 输入：s = ""
# 输出：0

class Solution:
    def longestValidParentheses(self, s):
        max_len = 0
        left_arrow_inds = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                left_arrow_inds.append(i)
            elif ch == ')':
                if len(left_arrow_inds) >= 2:
                    left_arrow_inds.pop()
                    curr_len = i - left_arrow_inds[-1]
                    max_len = max(max_len, curr_len)
                else:
                    left_arrow_inds[0] = i
        return max_len

if __name__ == '__main__':
    print(Solution().longestValidParentheses('(()'))
    print(Solution().longestValidParentheses('(()()'))
    print(Solution().longestValidParentheses(')()'))
    print(Solution().longestValidParentheses(')()())'))
    print(Solution().longestValidParentheses(')()())((())))'))
    print(Solution().longestValidParentheses(''))
