# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

# 示例 1：
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]

# 示例 2：
# 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]

# 示例 3：
# 输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]

# 提示：
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj 由小写英文字母与数字组成

class Node(object):
    def __init__(self):
        self.next = {}

class Solution:

    def calcEquation(self, equations, values, queries):
        node_dict = dict()
        n = len(values)
        for i in range(n):

            Ai, Bi = equations[i]
            val = values[i]

            if Ai in node_dict:
                node_A = node_dict[Ai]
            else:
                node_A = Node()
                node_dict[Ai] = node_A
            if Bi in node_dict:
                node_B = node_dict[Bi]
            else:
                node_B = Node()
                node_dict[Bi] = node_B

            node_A.next[Bi] = val
            node_B.next[Ai] = 1 / val

        all_nodes = set(node_dict.keys())
        all_root_nodes = []
        while len(all_nodes) > 0:
            root_node_id = all_nodes.pop()
            root_node = {root_node_id: 1.0}
            all_root_nodes.append(root_node)

            # BFS from root node
            queue = [(node_dict[root_node_id], 1)]
            while len(queue) > 0:
                node, ratio = queue.pop(0)
                for child, val in node.next.items():
                    if child not in root_node:
                        all_nodes.remove(child)
                        root_node[child] = ratio * val
                        queue.append((node_dict[child], ratio * val))

        ans = []
        for Ci, Di in queries:
            if Ci in node_dict and Di in node_dict:
                for root_node in all_root_nodes:
                    if Ci in root_node and Di in root_node:
                        ans.append(root_node[Di] / root_node[Ci])
                        break
                    elif (Ci in root_node) ^ (Di in root_node):
                        ans.append(-1.0)
                        break
            else:
                ans.append(-1.0)
        return ans

if __name__ == '__main__':
    # print(Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    print(Solution().calcEquation([["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]]))






