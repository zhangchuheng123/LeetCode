# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

# 示例 1：
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]

# 示例 2：
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]

# 提示：

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] 是一个小写英文字母
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同

WORD_FLAG = '$'

class Solution:
    def findWords(self, board, words):
        
        m, n = len(board), len(board[0])

        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node[WORD_FLAG] = word

        self.ans = set([])
        self.visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.visited[i][j] = True
                self.dfs(board, [i, j], [m, n], root)
                self.visited[i][j] = False

        return list(self.ans)

    def dfs(self, board, pos, size, node):
        ch = board[pos[0]][pos[1]]
        if ch in node:
            if WORD_FLAG in node[ch]:
                self.ans.add(node[ch][WORD_FLAG])
            for pos_delta in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_pos = [pos[0] + pos_delta[0], pos[1] + pos_delta[1]]
                if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < size[0] \
                    and new_pos[1] < size[1] and not self.visited[new_pos[0]][new_pos[1]]:
                    self.visited[new_pos[0]][new_pos[1]] = True
                    self.dfs(board, new_pos, size, node[ch])
                    self.visited[new_pos[0]][new_pos[1]] = False