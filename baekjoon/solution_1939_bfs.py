import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        numVertices, numEdges = map(int, input().split())
        adjacentList = [[] for _ in range(numVertices + 1)]
        for _ in range(numEdges):
            src, dst, weight = map(int, input().split())
            adjacentList[src].append((weight, dst)) # adjacentList - src: (weight, dst)
            adjacentList[dst].append((weight, src))

        oneEnd, oppositeEnd = map(int, input().split())

        self.findMaximumWeight(adjacentList, oneEnd, oppositeEnd, numVertices)

    def findMaximumWeight(self, adjacentList: list, oneEnd: int, oppositeEnd: int, numVertices: int) -> None:
        
        def bfs(mid: int) -> bool:
            queue = deque()
            queue.append(oneEnd)
            visited = [False] * (numVertices + 1)

            while queue:
                now = queue.popleft()

                if now == oppositeEnd:
                    return True

                for weight, next in adjacentList[now]:
                    if mid <= weight and visited[next] == False:
                        visited[next] = True
                        queue.append(next)
            
            return False

        start = 1
        end = 1_000_000_000

        ans = 1
        while start <= end:
            mid = start + (end - start) // 2

            if bfs(mid):
                start = mid + 1
                ans = mid

            else:
                end = mid - 1

        print(ans)

Solution()