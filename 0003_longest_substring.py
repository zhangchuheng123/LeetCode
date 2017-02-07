class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start_pos = 0
        ch_pos_dict = {}
        for now_pos in range(0, len(s)):
            ch = s[now_pos]
            if ch not in ch_pos_dict:
                now_len = now_pos - start_pos + 1
                max_len = max(max_len, now_len)
            else:
                last_pos = ch_pos_dict[ch]
                start_pos = max(start_pos, last_pos+1)
                now_len = now_pos - start_pos + 1
                max_len = max(max_len, now_len)
            ch_pos_dict.update({ch: now_pos})
        return max_len

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('bbbb'))
    print(solution.lengthOfLongestSubstring('pwwkew'))
    print(solution.lengthOfLongestSubstring('abcdefg'))
    print(solution.lengthOfLongestSubstring('abcdefgg'))
    print(solution.lengthOfLongestSubstring('aabbccddeeeff'))

