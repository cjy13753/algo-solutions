import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

class Solution:
    def __init__(self) -> None:
        rowNum, colNum = map(int, input().split())
        graph = [list(map(int, input().split()))for _ in range(rowNum)]

        self.maxPaths(rowNum, colNum, graph)

    def maxPaths(self, rowNum: int, colNum: int, graph: list):
        dp = [[-1] * colNum for _ in range(rowNum)]
        dp[0][0] = 1

        def dfs(row: int, col: int):
            if dp[row][col] != -1:
                return dp[row][col]
            if row == 0 and col == 0:
                return dp[0][0]
            
            tmpSum = 0
            for dRow, dCol in (0, 1), (1, 0), (0, -1), (-1, 0):
                neighborRow = row + dRow
                neighborCol = col + dCol

                if 0 <= neighborRow < rowNum and 0 <= neighborCol < colNum:
                    if graph[row][col] < graph[neighborRow][neighborCol]:
                        tmpSum += dfs(neighborRow, neighborCol)
                
            dp[row][col] = tmpSum
            return dp[row][col]

        print(dfs(rowNum - 1, colNum - 1))


Solution()