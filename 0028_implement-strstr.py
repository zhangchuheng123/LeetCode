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

# i=0, m=6, pi[6]=3, x=7-3-1=3
# abcabcabcx
# abcabcx

# abcabcabcx
#    abcabcx

# aaaa
# aaaaa

# missisippi
#        pi

# 总结：凡是有 index 的地方都要检查越界！
# 前缀函数的计算一定要注意，并不是只依赖于前一个，而是要递归依赖前面的


class Solution:
    def strStr(self, haystack, needle):

        l1, l2 = len(haystack), len(needle)

        if l2 == 0:
            return 0

        pi = [0]
        for j in range(1, l2):
            m = pi[-1]
            while needle[m] != needle[j] and m > 0:
                m = pi[m-1]
            if needle[m] == needle[j]:
                pi.append(m + 1)
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

            if m <= 1:
                i += 1
                m = 0
            else:
                x = m - pi[m-1]
                i = i + x
                m = pi[m-1]

        return -1

if __name__ == '__main__':
    print(str(Solution().strStr('hello', 'll')) + '=2')
    print(str(Solution().strStr('aaaa', 'aaaaa')) + '=-1')
    print(str(Solution().strStr('missisippi', 'pi')) + '=8')
    print(str(Solution().strStr('abcabcabcx',  'abcabcx')) + '=3')
    print(str(Solution().strStr('aabaaabaaac', 'aabaaac')) + '=4')

