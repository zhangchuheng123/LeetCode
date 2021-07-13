# [73, 74, 75, 71, 69, 72, 76, 73]
# [1,  1,  4,  2,  1,  1,  0,  0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            while len(stack) > 0 and stack[-1][1] <= temp:
                stack.pop()
            ans.insert(0, 0 if len(stack) == 0 else stack[-1][0] - i)
            stack.append((i, temp))
        return ans

if __name__ == '__main__':
    print(Solution().dailyTemperatures([89, 62, 70 ,58 ,47, 47, 46, 76, 100, 70]))