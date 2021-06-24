class Solution:
    def largestRectangleArea(self, heights):

        length = len(heights)
        left_delim = []
        right_delim = []

        stack = [(0, -1)]
        for i, h in enumerate(heights):
            while h <= stack[-1][0]:
                stack.pop()
            left_delim.append(stack[-1][1])
            stack.append((h, i))

        stack = [(0, length)]
        for j, h in enumerate(reversed(heights)):
            i = length - j - 1
            while h <= stack[-1][0]:
                stack.pop()
            right_delim.insert(0, stack[-1][1])
            stack.append((h, i))

        max_area = 0
        for i in range(length):
            area = (right_delim[i] - left_delim[i] - 1) * heights[i]
            if area > max_area:
                max_area = area
        return max_area