import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    ySize, xSize = map(int, input().split())
    forestMap = [[0] * xSize for _ in range(ySize)]

    beaver = [0, 0]

    qWater = deque()
    qHedgeHog = deque()

    for y in range(ySize):
        for x, val in enumerate(input().strip()): # beaver는 -4, Rock은 -3, water는 -2, 빈 곳이면 -1, hedgeHog는 0
            if val == "D":
                beaver[0], beaver[1] = y, x
                forestMap[y][x] = -4
            elif val == 'X':
                forestMap[y][x] = -3
            elif val == '*':
                qWater.append((y, x))
                forestMap[y][x] = -2
            elif val == ".":
                forestMap[y][x] = -1
            elif val == "S":
                qHedgeHog.append((y, x))
                forestMap[y][x] = 0

    dY = [0, 1, 0, -1] # 동, 남, 서, 북
    dX = [1, 0, -1, 0]
    
    while qWater or qHedgeHog:
        for i in range(len(qWater)):
            oY, oX = qWater.popleft()

            for i in range(4):
                nY = oY + dY[i]
                nX = oX + dX[i]

                if 0 <= nY < ySize and 0 <= nX < xSize and forestMap[nY][nX] == -1:
                    forestMap[nY][nX] = -2
                    qWater.append((nY, nX))

        for i in range(len(qHedgeHog)):
            oY, oX = qHedgeHog.popleft()

            for i in range(4):
                nY = oY + dY[i]
                nX = oX + dX[i]

                if 0 <= nY < ySize and 0 <= nX < xSize and (forestMap[nY][nX] == -1 or forestMap[nY][nX] == -4):
                    forestMap[nY][nX] = forestMap[oY][oX] + 1
                    qHedgeHog.append((nY, nX))
    
    ans = forestMap[beaver[0]][beaver[1]]
    if ans == -4:
        print('KAKTUS')
    else:
        print(ans)