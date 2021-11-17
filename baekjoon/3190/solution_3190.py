import sys
from collections import deque

boardSize = int(sys.stdin.readline())
board = [[0] * boardSize for _ in range(boardSize)]
numApples = int(sys.stdin.readline())
for _ in range(numApples):
    rowApple, colApple = list(map(int, sys.stdin.readline().split()))
    board[rowApple - 1][colApple - 1] = 1
numTurns = int(sys.stdin.readline())
turns = {}
for _ in range(numTurns):
    time, turnDirection = sys.stdin.readline().split()
    turns[int(time)] = turnDirection

direction = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = deque([[0,0]])
time = 0

while True:
    time += 1
    row = visited[0][0] + dx[direction]
    col = visited[0][1] + dy[direction]

    # snake가 벽에 닿으면 게임 종료
    if row < 0 or row >= boardSize or col < 0 or col >= boardSize:
        break
    
    # snake가 자기 자신을 만나면 게임 종료
    if board[row][col] == 2:
        break

    # 사과 먹으면 사과 없애주기, 사과를 안 먹으면 꼬리가 잘림
    if board[row][col] == 1:
        board[row][col] = 0        
    else:
        tailRow, tailCol = visited.pop()
        board[tailRow][tailCol] = 0

    # 아무 문제 없으면 머리를 적절한 방향으로 한 칸 확장하기
    board[row][col] = 2
    visited.appendleft([row, col])

    # 적절한 시간이 되면 방향이 바뀜
    if time in turns.keys():
        if turns[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
print(time)