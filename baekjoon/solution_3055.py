import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    ySize, xSize = map(int, input().split())
    forestMap = [[0] * xSize for _ in range(ySize)]
    INF = int(1e10)

    hedgeHog = [0, 0]
    beaver = [0, 0]
    waterQueue = deque()
    hedgeHogQueue = deque()


    for y in range(ySize):
        for x, val in enumerate(input().strip()):
            if val == "D":
                beaver[0], beaver[1] = y, x
                forestMap[y][x] = INF
            elif val == "S":
                hedgeHog[0], hedgeHog[1] = y, x
                hedgeHogQueue.append((y, x))
            elif val == 'X':
                forestMap[y][x] = INF
            elif val == '*':
                waterQueue.append((y, x))
            else:
                forestMap[y][x] = 0

    dY = [0, 1, 0, -1] # 동, 남, 서, 북
    dX = [1, 0, -1, 0]
    # 먼저 물로 범람시켜놓기
    while waterQueue:
        oY, oX = waterQueue.popleft()

        for i in range(4):
            nY = oY + dY[i]
            nX = oX + dX[i]

            if 0 <= nY < ySize and 0 <= nX < xSize and forestMap[nY][nX] == 0:
                forestMap[nY][nX] = forestMap[oY][oX] + 1
                waterQueue.append((nY, nX))
    
    # 고슴도치 이동시키기
    forestMap[hedgeHog[0]][hedgeHog[1]] = -2 # 초기화
    while hedgeHogQueue:
        oY, oX = hedgeHogQueue.popleft()

        for i in range(4):
            nY = oY + dY[i]
            nX = oX + dX[i]

            if 0 <= nY < ySize and 0 <= nX < xSize:
                if forestMap[oY][oX] + 1 < forestMap[nY][nX]:
                    forestMap[nY][nX] = forestMap[oY][oX] + 1
                    hedgeHogQueue.append((nY, nX))

    ans = forestMap[beaver[0]][beaver[1]]
    if ans == INF:
        print('KAKTUS')
    else:
        print(ans+2)