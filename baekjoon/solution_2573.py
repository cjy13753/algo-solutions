import sys
from typing import List
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def solution(iceberg: list, rowNum: int, colNum: int) -> int:
    year = 0

    def meltAround(row: int, col: int, rowNum: int, colNum: int) -> None:
        directions = [0, 1, 0, -1, 0]
        for i in range(len(directions) - 1):
            newRow = row + directions[i]
            newCol = col + directions[i + 1]
            if newRow >= 0 and newRow < rowNum and newCol >= 0 and newCol < colNum and iceberg[newRow][newCol] > 0:
                iceberg[newRow][newCol] -= 1

    def dfs(visited: List[List[bool]], row: int, col: int, rowNum: int, colNum: int) -> None:
        visited[row][col] = True
        directions = [0, 1, 0, -1, 0]
        for i in range(len(directions) - 1):
            newRow = row + directions[i]
            newCol = col + directions[i + 1]
            if newRow >= 0 and newRow < rowNum and newCol >= 0 and newCol < colNum:
                if visited[newRow][newCol] == False and iceberg[newRow][newCol] > 0:
                    dfs(visited, newRow, newCol, rowNum, colNum)
        

    while True:
        emptyIcebergList = []
        for row in range(rowNum):
            for col in range(colNum):
                if iceberg[row][col] == 0:
                    emptyIcebergList.append(([row, col]))
        
        # 1년 지날 때마다 빙산이 녹는다. 빙산이 높이가 1 이상인 것들에 대해서만 녹이는 작업을 진행해준다
        for row, col in emptyIcebergList:
            meltAround(row, col, rowNum, colNum)
        year += 1

        # 매 loop를 돌 때마다 visited 배열의 요소들을 전부 False로 초기화시켜준다
        visited = [[False] * colNum for _ in range(rowNum)]
        count = 0
        # 빙산을 녹이고 난 직후 덩어리가 2개 이상으로 분리됐는지 확인해준다.
        for row in range(rowNum):
            for col in range(colNum):
                if iceberg[row][col] > 0 and visited[row][col] == False:
                    count += 1
                    dfs(visited, row, col, rowNum, colNum)
        # 덩어리의 개수를 count로 세고, count가 0이 될 때까지 loop를 돌리고, 만약 count가 2 이상이 되는 순간 loop를 break한다.
        if count >= 2:
            break
        if count == 0:
            break
    
    return year

if __name__ == "__main__":
    rowNum, colNum = map(int, input().split())
    iceberg = []
    for i in range(rowNum):
        iceberg.append(list(map(int, input().split())))

    print(solution(iceberg, rowNum, colNum))