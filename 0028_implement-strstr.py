# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

# 当 needle 是空字符串时，返回 0

# 输入：haystack = "hello", needle = "ll"
# 输出：2

# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1

# 输入：haystack = "", needle = ""
# 输出：0

# 思路：暴力方法是做滑动窗口，一个个判断；这里考虑判断失败之后，能够跳过一些字符的比较。
# 假设目前匹配了 haystack[i:i+m] 和 needle[:m]，但是 haystack[i+m] != needle[m]
# 现在希望能直接把 haystack[i+x:i+m] 和 needle[:x] 匹配起来，然后接着往下走
# 可以通过前缀函数来找到这样的 x，x = m - pi[m-1] - 1
# 前缀函数可以递归找到

# i=0, m=7, pi[6]=3, x=7-3-1=3
# abcabcd
# abcabcx

# abcabca
#    abcabcx

# aaaa
# aaaaa

# 总结：凡是有 index 的地方都要检查越界！


class Solution:
    def strStr(self, haystack, needle):

        l1, l2 = len(haystack), len(needle)

        if l2 == 0:
            return 0

        pi = [0]
        for j in range(1, l2):
            if needle[pi[-1]] == needle[j]:
                pi.append(pi[-1] + 1)
            else:
                pi.append(0)

        i = 0
        m = 0
        while i < l1:
            while m < l2 and i+m < l1 and haystack[i+m] == needle[m]:
                m += 1

            if m == l2:
                return i
            elif  i+m == l1:
                return -1

            if m == 0:
                i += 1
            else:
                x = m - pi[m-1] - 1
                i = i + x
                m = pi[m-1]

        return -1