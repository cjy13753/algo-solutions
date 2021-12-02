import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        rowNum, colNum = map(int, input().split())
        graph = [list(map(int, input().split()))for _ in range(rowNum)]

        self.maxPaths(rowNum, colNum, graph)

    def maxPaths(self, rowNum: int, colNum: int, graph: list):
        dp = [[0] * colNum for _ in range(rowNum)]
        dp[0][0] = 1
        queue = deque()
        queue.append((1, 0))
        queue.append((0, 1))

        while queue:
            sum = 0
            row, col = queue.popleft()

            for dRow, dCol in (0, 1), (1, 0), (0, -1), (-1, 0):
                neighborRow = row + dRow
                neighborCol = col + dCol

                if 0 <= neighborRow < rowNum and 0 <= neighborCol < colNum:
                    if  graph[row][col] < graph[neighborRow][neighborCol]:
                        sum += dp[neighborRow][neighborCol]
                    elif graph[row][col] > graph[neighborRow][neighborCol]:
                        queue.append((neighborRow, neighborCol))
            
            dp[row][col] = max(dp[row][col], sum)

        print(dp[rowNum - 1][colNum - 1])


Solution()