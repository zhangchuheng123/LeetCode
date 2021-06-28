class Solution:
    def search(self, s, ind, ind2list, wordDict):
        ans = []
        for word in wordDict:
            endind = ind + len(word)
            if s[ind:endind] == word:
                if endind == len(s):
                    strlist = [word]
                else:
                    if endind not in ind2list:
                        strlist = self.search(s, endind, ind2list, wordDict)
                        ind2list[endind] = strlist
                    else:
                        strlist = ind2list[endind]
                    strlist = strlist.copy()
                    strlist = [word + ' ' + string for string in strlist]
                ans += strlist
        return ans

    def wordBreak(self, s, wordDict):
        ind2list = dict()
        if len(s) == 0:
            return []
        ans = self.search(s, 0, ind2list, wordDict)
        return ans

if __name__ == '__main__':
    print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
    print(Solution().wordBreak("aaaaaaa", ["aaaa", "aa", "a"]))