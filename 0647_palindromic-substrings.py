class Solution:
    def countSubstrings(self, s):
        right_most = -1
        right_most_center = -1
        ans = 0

        string = '%#' + '#'.join(list(s)) + '#&'
        f = [0] * len(string)
        for i in range(2, len(string) - 2):
            if i < right_most:
                 f[i] = min(f[2 * right_most_center - i], right_most - i)
            span = f[i] + 1
            while string[i - span] == string[i + span]:
                span += 1
            f[i] = span - 1
            if i + f[i] > right_most:
                right_most = i + f[i]
                right_most_center = i
            ans += (f[i] + 1) // 2

        return ans

if __name__ == '__main__':
    print(Solution().countSubstrings('abc'))
    print(Solution().countSubstrings('aaaa'))
    print(Solution().countSubstrings('abcba'))
    print(Solution().countSubstrings('abcbad'))
    print(Solution().countSubstrings('dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg'))