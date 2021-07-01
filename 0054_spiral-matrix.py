# R = 0
# D = 1
# L = 2
# U = 3

import pdb

class Solution:
    def spiralOrder(self, matrix):

        # def next(status):
        #     if status == R:
        #         return D
        #     elif status == D:
        #         return L
        #     elif status == L:
        #         return U
        #     elif status == U:
        #         return R

        def next(status):
            return (status + 1) % 4

        def next_position(pos, status):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            return [pos[0] + directions[status][0], pos[1] + directions[status][1]]

        l, r, u, d = -1, len(matrix[0]), 0, len(matrix)
        status = 0
        pos = [0, 0]

        ans = []
        while True:
            ans.append(matrix[pos[0]][pos[1]])
            next_pos = next_position(pos, status)
            if status == 0 and next_pos[1] >= r:
                status = next(status)
                next_pos = next_position(pos, status)
                if next_pos[0] >= d:
                    break
                r -= 1
            elif status == 1 and next_pos[0] >= d:
                status = next(status)
                next_pos = next_position(pos, status)
                if next_pos[1] <= l:
                    break
                d -= 1
            elif status == 2 and next_pos[1] <= l:
                status = next(status)
                next_pos = next_position(pos, status)
                if next_pos[0] <= u:
                    break
                l += 1
            elif status == 3 and next_pos[0] <= u:
                status = next(status)
                next_pos = next_position(pos, status)
                if next_pos[1] >= r:
                    break
                u += 1

            pos = next_pos

        return ans

if __name__ == '__main__':
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))