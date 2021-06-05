class Solution:
    def longestCommonPrefix(self, strs):
        common = []
        minlen = 200
        for s in strs:
            minlen = min(minlen, len(s))
        s0 = strs[0]
        for i in range(minlen):
            for s in strs[1:]:
                if s[i] != s0[i]:
                    return ''.join(common)
            common.append(s0[i])
        return ''.join(common)