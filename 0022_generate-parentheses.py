class Solution:
    def generateParenthesis(self, n):

        def generate(n, nleft, nright, s):

            if nleft == n and nright == n:
                return [s]

            if nleft < n:
                l1 = generate(n, nleft+1, nright, s + '(')
            else:
                l1 = []

            if nright < nleft:
                l2 = generate(n, nleft, nright+1, s + ')')
            else:
                l2 = []

            return l1 + l2

        return generate(n, 0, 0, '')

if __name__ == '__main__':
    for i in range(8):
        solution = Solution()
        print(solution.generateParenthesis(i))
