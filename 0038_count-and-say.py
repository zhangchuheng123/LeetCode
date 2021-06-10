
ORD0 = 48

class Solution:
    def countAndSay(self, n):
        string = '1'
        for i in range(n - 1):
            string = self.waiguan(string)
        return string

    @staticmethod
    def waiguan(string):

        ans = []

        n = len(string)
        string += 'a'
        i = 0
        j = 1

        while j <= n:
            if string[j] == string[i]:
                j += 1
            else:
                count = j - i
                num = string[i]
                ans.append(chr(count + ORD0))
                ans.append(num)
                i = j
                j += 1

        return ''.join(ans)

if __name__ == '__main__':
    print(Solution().countAndSay(1))
    print(Solution().countAndSay(2))
    print(Solution().countAndSay(3))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(5))
    print(Solution().countAndSay(6))
    print(Solution().countAndSay(7))
