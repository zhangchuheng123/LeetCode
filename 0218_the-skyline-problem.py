# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

# 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

# lefti 是第 i 座建筑物左边缘的 x 坐标。
# righti 是第 i 座建筑物右边缘的 x 坐标。
# heighti 是第 i 座建筑物的高度。
# 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

# 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

# 示例 1：


# 输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# 解释：
# 图 A 显示输入的所有建筑物的位置和高度，
# 图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
# 示例 2：

# 输入：buildings = [[0,2,3],[2,5,3]]
# 输出：[[0,3],[5,0]]

# 提示：

# 1 <= buildings.length <= 104
# 0 <= lefti < righti <= 231 - 1
# 1 <= heighti <= 231 - 1
# buildings 按 lefti 非递减排序

# class Solution:
#     def getSkyline(self, buildings):
#         queue = deque()
#         ans = []
#         for left, right, height in buildings:

#             # Step 1: pop solved points
#             last_h = 0
#             while len(queue) > 0 and queue[0][0] < left:
#                 last_loc, last_h = queue.popleft()
#                 if len(ans) == 0 or ans[-1][1] != last_h:
#                     ans.append([last_loc, last_h])

#             # Step 2: try to update/add left point
#             i = 0
#             if len(queue) > 0 and queue[0][0] == left:
#                 last_h = queue[0][1]
#                 queue[0][1] = max(last_h, height)
#             else:
#                 if height > last_h:
#                     queue.appendleft([left, height])
#                     i += 1

#             # Step 3: update points between left and right
#             while i < len(queue):
#                 if queue[i][0] < right:
#                     last_h = queue[i][1]
#                     queue[i][1] = max(last_h, height)
#                     i += 1
#                 else:
#                     break

#             # Step 4: try to update/add right point
#             if i >= len(queue) or queue[i][0] > right:
#                 queue.insert(i, [right, last_h])

#             print(left, right, height, queue, ans)


#         while len(queue) > 0:
#             last_loc, last_h = queue.popleft()
#             if len(ans) == 0 or ans[-1][1] != last_h:
#                 ans.append([last_loc, last_h])

#         return ans

# from collections import deque


# class Solution:

#     @staticmethod
#     def move(keypoints, ans):
#         if len(ans) == 0 or ans[-1][1] != keypoints[0][1]:
#             ans.append(keypoints.popleft())
#         else:
#             keypoints.popleft()

#     def getSkyline(self, buildings):

#         ans = []

#         keypoints = [l for l, _, _ in buildings] + [r for _, r, _, in buildings]
#         keypoints = sorted(list(set(keypoints)))
#         keypoints = deque([[p, 0] for p in keypoints])

#         for left, right, height in buildings:

#             while keypoints[0][0] < left:
#                 self.move(keypoints, ans)

#             i = 0
#             while keypoints[i][0] < right:
#                 keypoints[i][1] = max(keypoints[i][1], height)
#                 i += 1

#         while len(keypoints) > 0:
#             self.move(keypoints, ans)
#         return ans

import heapq

class Solution:

    def getSkyline(self, buildings):
        keypoints = [(l, -h, r) for l, r, h in buildings] + [(r, 0, 0) for _, r, _ in buildings]
        keypoints.sort()

        ans = []
        # maintain a min heap for all the buildings span over the current point (-h, r)
        heap = [(0, float('inf'))]
        for x, neg_h, r in keypoints:
            h = - neg_h
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if h > 0:
                heapq.heappush(heap, (neg_h, r))
            if len(ans) == 0 or ans[-1][1] != -heap[0][0]:
                ans.append([x, -heap[0][0]])
        return ans


if __name__ == '__main__':
    print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    print(Solution().getSkyline([[0,2,3],[2,5,3]]))
