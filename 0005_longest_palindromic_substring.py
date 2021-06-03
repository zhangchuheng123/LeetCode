class Solution:
    def center_expand(self, s, length, c1, c2):
        while c1 - 1 >= 0 and c2 + 1 < length and s[c1-1] == s[c2+1]:
            c1 -= 1
            c2 += 1
        return c1, c2

    def longestPalindrome(self, s):

        length = len(s)
        begin, end = 0, 0
        for center in range(length):
            l1, r1 = self.center_expand(s, length, center, center)
            if r1 - l1 > end - begin:
                begin, end = l1, r1
            if center + 1 < length and s[center] == s[center+1]:
                l2, r2 = self.center_expand(s, length, center, center + 1)
                if r2 - l2 > end - begin:
                    begin, end = l2, r2

        return s[begin:end+1]

# This can be further improve by considering the example:
# xxxaxcxaxxx
# If this is a palindromic substring, xax is checked once. 
# So when we move to using a as the center, we can skip checking xax.