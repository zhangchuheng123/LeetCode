class Solution:
    def search(self, position, word, board, width, height, visited):
        if len(word) == 0:
            return True

        for test_position in [[position[0] - 1, position[1]], [position[0] + 1, position[1]], \
            [position[0], position[1] - 1], [position[0], position[1] + 1]]:

            if test_position[0] >= 0 and test_position[0] < height \
                and test_position[1] >= 0 and test_position[1] < width \
                and board[test_position[0]][test_position[1]] == word[0] \
                and (not visited[test_position[0]][test_position[1]]):

                visited[test_position[0]][test_position[1]] = True
                if self.search(test_position, word[1:], board, width, height, visited):
                    return True
                visited[test_position[0]][test_position[1]] = False

        return False

    def exist(self, board, word):
        height = len(board)
        width = len(board[0])
        visited = [[False for _ in range(width)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.search([i, j], word[1:], board, width, height, visited):
                        return True
                    visited[i][j] = False
        return False
