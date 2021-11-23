import sys
from collections import deque
from functools import reduce
input = sys.stdin.readline


def calPassedTime(tomatoBox: list):
    maxTime = int(-1e10)
    for z in tomatoBox:
        for y in z:
            product = reduce(lambda a,b: a*b, y)
            if product == 0:
                return -1
            else:
                maxTime = max(maxTime, max(y))
    return maxTime - 1

if __name__ == '__main__':
    xSize, ySize, zSize = map(int, input().split())
    tomatoBox = [[[0] * xSize for _ in range(ySize)] for _ in range(zSize)] # appleBox[z][y][x]
    queue = deque()
    
    for z in range(zSize):
        for y in range(ySize):
            for x, val in enumerate(map(int, input().split())): # 1: 익은 토마토, 0: 익지 않은 토마토, -1: 사과 없음
                if val == 1:
                    queue.append((z, y, x))
                tomatoBox[z][y][x] = val

    dZ = [0, 0, 0, 0, 1, -1] # 동, 남, 서, 북, 상, 하
    dY = [0, -1, 0, 1, 0, 0]
    dX = [1, 0, -1, 0, 0, 0] 

    while queue:
        oZ, oY, oX= queue.popleft()

        for i in range(6):
            nZ = oZ + dZ[i]
            nY = oY + dY[i]
            nX = oX + dX[i]

            if 0 <= nZ < zSize and 0 <= nY < ySize and 0 <= nX < xSize:
                if tomatoBox[nZ][nY][nX] == 0:
                    tomatoBox[nZ][nY][nX] = tomatoBox[oZ][oY][oX] + 1
                    queue.append((nZ, nY, nX))

    print(calPassedTime(tomatoBox))