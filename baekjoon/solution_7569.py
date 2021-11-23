import sys
from collections import deque
import copy
input = sys.stdin.readline


def validate(appleBox: list): # 박스 내 사과 상태 체크하는 로직. 출력: 다 익었으면 1, 다 안 익었고 익을 수 있는 상황이면 0, 다 익을 수 없는 상황이면 -1.
    z = len(appleBox)
    y = len(appleBox[0])
    x = len(appleBox[0][0])

    dZ = [0, 0, 0, 0, 1, -1] # 동, 남, 서, 북, 상, 하
    dY = [0, -1, 0, 1, 0, 0]
    dX = [1, 0, -1, 0, 0, 0] 

    visited = [[[False] * x for _ in range(y)] for _ in range(z)]
    appleBox = copy.deepcopy(appleBox)

    def bfs(i, j, k):
        queue = deque()
        queue.append((i, j, k))

        while queue:
            oZ, oY, oX = queue.pop()

            visited[oZ][oY][oX] = True
            appleBox[oZ][oY][oX] = 1

            for i in range(len(dZ)):
                nZ = oZ + dZ[i]
                nY = oY + dY[i]
                nX = oX + dX[i]

                if nZ >= 0 and nZ < z and nY >= 0 and nY < y and nX >= 0 and nX < x:
                    if appleBox[nZ][nY][nX] != -1 and visited[nZ][nY][nX] == False:
                        queue.append((nZ, nY, nX))

    unripeCount = 0
    for i in range(z):
        for j in range(y):
            for k in range(x):
                if appleBox[i][j][k] == 0:
                    unripeCount += 1
    
    if unripeCount == 0:
        return 1

    for i in range(z):
        for j in range(y):
            for k in range(x):
                if appleBox[i][j][k] == 1 and visited[i][j][k] == False:
                    bfs(i, j, k)

    product = 1
    for i in range(z):
        for j in range(y):
            for k in range(x):
                product *= appleBox[i][j][k]
    
    if product == 0:
        return -1
    else:
        return 0

def ripen(appleBox: list) -> None:
    z = len(appleBox)
    y = len(appleBox[0])
    x = len(appleBox[0][0])

    dZ = [0, 0, 0, 0, 1, -1] # 동, 남, 서, 북, 상, 하
    dY = [0, -1, 0, 1, 0, 0]
    dX = [1, 0, -1, 0, 0, 0] 

    for i in range(z):
        for j in range(y):
            for k in range(x):
                if appleBox[i][j][k] == 0:
                    for p in range(len(dZ)):
                        nI = i + dZ[p]
                        nJ = j + dY[p]
                        nK = k + dX[p]
                        if nI >= 0 and nI < z and nJ >= 0 and nJ < y and nK >= 0 and nK < x:
                            if appleBox[nI][nJ][nK] == 1:
                                appleBox[i][j][k] = 1
                                continue

if __name__ == '__main__':
    x, y, z = map(int, input().split())
    appleBox = [[] for _ in range(z)] # appleBox[z][y][x]
    for i in range(z):
        for _ in range(y):
            appleBox[i].append(list(map(int, input().split()))) # 1: 익은 토마토, 0: 익지 않은 토마토, -1: 사과 없음

    days = 0
    # 시작하자마자 다 익었는지 체크. 시작하자마자 다 익었으면 0 출력, 토마토가 모두 익지 못하는 상황이면 -1 출력
    while True:
        validityCheck = validate(appleBox)
        if validityCheck == -1:
            print(-1)
            break
        elif validityCheck == 1:
            print(days)
            break
        else:
            ripen(appleBox)
            days += 1






