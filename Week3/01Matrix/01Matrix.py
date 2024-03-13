from math import inf
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        if not mat :
            return mat

        directions = [[0,-1], [0,1], [1, 0], [-1, 0]]
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = inf
        
        #bfs
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c, = row + dr, col + dc
                if 0 <= r < len(mat) and 0 <= c < len(mat[0]) and mat[r][c] > mat [row][col] + 1:
                    queue.append((r, c))
                    mat[r][c] = mat[row][col] + 1

        return mat
