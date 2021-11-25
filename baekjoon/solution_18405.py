import sys
from collections import deque
input = sys.stdin.readline

# checkIfPresent를 계속 돌림
# 최초 작업: queue(deque)를 생성하고, 행렬을 돌면서 바이러스들을 모두 deque에 넣어준다
# 다음으로 queue 오름차순으로 정렬해준다. 정렬해주는 이유는 번호가 낮은 바이러스부터 퍼지게 하기 위함
# queue의 크기 만큼만 바이러스 확산을 시켜준다.

if __name__ == '__main__':
    boardSize, numVirusTypes = map(int, input().split())
    board = [[0] * (boardSize + 1)]
    for _ in range(boardSize):
        board.append(list(map(int, ("0 " + input()).split())))

    secondsPassed, xRes, yRes = map(int, input().split())
    
    viruses = []
    for i in range(1, boardSize + 1):
        for j in range(1, boardSize + 1):
            if board[i][j] > 0:
                viruses.append([board[i][j], i, j]) # viruses: [virusType, x, y]
    viruses.sort()
    viruses = deque(viruses)

    for i in range(secondsPassed):
        for _ in range(len(viruses)):
            virusType, x, y = viruses.popleft()

            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                nx = x + dx
                ny = y + dy
                if 0 < nx <= boardSize and 0 < ny <= boardSize:
                    if board[nx][ny] == 0:
                        board[nx][ny] = virusType
                        viruses.append([virusType, nx, ny])
    
    print(board[xRes][yRes])