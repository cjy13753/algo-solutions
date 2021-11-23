import sys
import heapq
input = sys.stdin.readline

def dijkstra(board: list) -> int:
    boardSize = len(board) - 1
    INF = float('inf')
    costTable = [[INF] * (boardSize + 1) for _ in range(boardSize + 1)]
    visited = [[False] * (boardSize + 1) for _ in range(boardSize + 1)]

    minHeap = [] # minHeap: (accumCost, now). now = (x, y)
    dX = [0, 1, 0, -1]
    dY = [1, 0, -1, 0]

    # 시작 점 초기화
    costTable[1][1] = 0
    heapq.heappush(minHeap, (0, (1, 1)))

    # 방문하지 않은 노드 중 누적 비용이 가장 작은 이미지
    while minHeap:
        accumCost, now = heapq.heappop(minHeap)
        x, y = now
        
        if visited[x][y] == True:
            if x == boardSize and y == boardSize:
                break
            continue

        visited[x][y] = True

        # 현재 노드를 경유한다고 했을 때 인접 노드로 도달할 때 비용이 기존 인접 노드로 도달하는 데 드는 비용보다 작다면 갱신해준다.
        for i in range(len(dX)):
            nX = x + dX[i]
            nY = y + dY[i]

            if nX > 0 and nX <= boardSize and nY > 0 and nY <= boardSize:
                newAccumCost = accumCost + (1 - board[nX][nY])
                if newAccumCost < costTable[nX][nY]:
                    costTable[nX][nY] = newAccumCost
                    next = (nX, nY)
                    heapq.heappush(minHeap, (newAccumCost, next))

    return costTable[boardSize][boardSize]

if __name__ == '__main__':
    boardSize = int(input())
    board = []
    board.append([0] * (boardSize + 1))
    for _ in range(boardSize):
        board.append(list(map(int, '0' + input().strip())))

    print(dijkstra(board))