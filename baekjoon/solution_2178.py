import sys
from collections import deque
input = sys.stdin.readline

def bfs(maze: list) -> int:
    rowSize = len(maze) - 1
    colSize = len(maze[0]) - 1
    dX = [0, 1, 0, -1]
    dY = [1, 0, -1, 0]

    queue = deque()
    queue.append((1, 1, 1)) # (row, col, total)
    visited = [[False] * (colSize + 1) for _ in range(rowSize + 1)]
    
    count = 10_000 # big enough random number
    while queue:
        row, col, total = queue.popleft()
        if row == rowSize and col == colSize:
            count = min(count, total)

        for i in range(len(dX)):
            nRow = row + dX[i]
            nCol = col + dY[i]
            if nRow > 0 and nRow <= rowSize and nCol > 0 and nCol <= colSize:
                if visited[nRow][nCol] == False and maze[nRow][nCol] == 1:
                    visited[nRow][nCol] = True                    
                    queue.append((nRow, nCol, total + 1))
    
    return count

if __name__ == '__main__':
    rowSize, colSize = map(int, input().split())
    maze = []
    maze.append([0] * (colSize + 1)) # dummy row 추가(one indexing 위함)
    for _ in range(rowSize):
        maze.append(list(map(int, "0"+input().strip())))

    print(bfs(maze))