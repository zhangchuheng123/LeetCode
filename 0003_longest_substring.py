# 暴力搜索: O(n^2) 个子串，每个子串还需要两两检查，最终 O(n^4)
# 分治法：合并的时候复杂度高
# 从左往右扫描，如果发现新加入的字符和前面的字符重复了，那么就刷新计数，并且重新从前面重复字符的下一个开始继续往右扫描，最终 O(n^2)

class Solution:
    def lengthOfLongestSubstring(self, s):

        length = len(s)
        maxlen = 0
        next_l, l, r = 0, 0, 1

        for l in range(length):

            # move to the next window
            if l < next_l:
                continue

            # find max substring starting at l
            while r < length and s[r] not in s[l:r]:
                r += 1
            # update maxlen
            maxlen = max(maxlen, r - l)

            # pre-process next window
            if r + 1 >= length:
                break
            else:
                next_l = l + s[l:r].index(s[r]) + 1
                r += 1

        return maxlen